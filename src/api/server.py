from fastapi import FastAPI, Query
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import numpy as np
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Autorise uniquement le frontend
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST...)
    allow_headers=["*"],  # Autorise tous les headers
)

# Charger les données
df = pd.read_csv("Global_dataset.csv", sep=";")
df = df.fillna("Donnée manquante")


# Convertir la colonne Date en datetime
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
# Trouver la dernière année disponible dans le dataset
last_year = int(df["Date"].dt.year.max())
# Filtrer les données pour la dernière année disponible
df_year = df[df["Date"].dt.year == last_year].copy()
# Extraire les derniers jours du dataset
df_recent = df.sort_values(by="Date", ascending=False).head(7)
# Conversion en numérique pour certaines colonnes
df["Admissions_totales"] = pd.to_numeric(df["Admissions_totales"], errors="coerce").fillna(0)


# Définition d'un mapping pour le filtre Service
services_mapping = {
    "Neurologie": "Patients_admis_en_Neurologie_et_neurosciences",
    "Psychiatrie": "Patients_admis_en_Psychiatrie",
    "Gériatrie": "Patients_admis_en_Gériatrie_et_soins_palliatifs",
    "Soins intensifs": "Patients_admis_en_Soins_intensifs",
    "Chirurgie": "Patients_admis_en_Chirurgie_et_transplantation",
    "Cardiologie": "Patients_admis_en_Cardilogie_et_médecine_vasculaire",
    "Urgences": "Admissions_urgences"
}

# Endpoint pour récupérer toutes les données
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# Simuler une prédiction avec une régression linéaire simple
def predict_taux_occupation():
    x = np.arange(len(df))  # Index des jours
    y = df["Lits_occupes"] / (df["Lits_disponibles"] + df["Lits_occupes"]) * 100  # Taux d'occupation en %

    # Modèle de régression linéaire
    coef = np.polyfit(x, y, 1)
    tendance = np.poly1d(coef)

    return round(tendance(len(df) + 1), 2)  # Prédiction du jour suivant

# Endpoint pour récupérer les données du dashboard
@app.get("/dashboard")
def get_dashboard():
    # Admissions Totales
    latest_data = df.iloc[-1]  # Aujourd’hui
    yesterday_data = df.iloc[-2]  # Hier

    admissions_jour = int(latest_data["Admissions_totales"])
    admissions_hier = int(yesterday_data["Admissions_totales"]) if not yesterday_data.empty else admissions_jour

    evolution_admissions = (
        round(((admissions_jour - admissions_hier) / admissions_hier) * 100, 2)
        if admissions_hier != 0 else 0
    )
    evolution_admissions = round(evolution_admissions)

    # Taux d’occupation des lits
    taux_occupation = round(
        (latest_data["Lits_occupes"] / (latest_data["Lits_disponibles"] + latest_data["Lits_occupes"])) * 100
    )
    taux_occupation_hier = round(
        (yesterday_data["Lits_occupes"] / (yesterday_data["Lits_disponibles"] + yesterday_data["Lits_occupes"])) * 100
    ) if not yesterday_data.empty else taux_occupation

    evolution_taux_occupation = taux_occupation - taux_occupation_hier

    # Prédiction du taux d'occupation des lits pour demain
    prediction_taux_occupation = round(predict_taux_occupation())

    # Temps d’attente moyen
    temps_attente_jour = int(latest_data["Temp_d’attente_moyen_minutes"])
    temps_attente_hier = int(yesterday_data["Temp_d’attente_moyen_minutes"]) if not yesterday_data.empty else temps_attente_jour

    evolution_temps_attente = (
        round(((temps_attente_jour - temps_attente_hier) / temps_attente_hier) * 100, 2)
        if temps_attente_hier != 0 else 0
    )
    evolution_temps_attente = round(evolution_temps_attente)

    return {
        "admissions_jour": admissions_jour,
        "evolution_admissions": f"{evolution_admissions}%",
        "taux_occupation": f"{taux_occupation}%",
        "evolution_taux_occupation": f"{evolution_taux_occupation}%",
        "prediction_taux_occupation": f"{prediction_taux_occupation}%",  # Valeur prédite
        "temps_attente_jour": f"{temps_attente_jour} min",
        "evolution_temps_attente": f"{evolution_temps_attente}%",
    }

# Endpoint pour récupérer l'évolution des admissions par mois
@app.get("/evolution-admissions")
def get_evolution_admissions():
    # Vérifier et convertir Admissions_totales en nombres valides
    df_year["Admissions_totales"] = pd.to_numeric(df_year["Admissions_totales"], errors="coerce").fillna(0)

    # Groupement par mois
    monthly_admissions = (
        df_year.groupby(df_year["Date"].dt.month)["Admissions_totales"]
        .sum()
        .reset_index()
    )

    mois_list = monthly_admissions["Date"].astype(int).tolist()
    admissions_list = monthly_admissions["Admissions_totales"].astype(float).astype(int).tolist()

    return {
        "mois": mois_list,
        "admissions": admissions_list,
        "annee": last_year,
    }

# Endpoint pour récupérer les statistiques des admissions avec filtres dynamiques
@app.get("/admissions")
def get_admissions(
    service: Optional[str] = Query(None, description="Service médical (ex: Neurologie, Urgences)"),
    date_debut: Optional[str] = Query(None, description="Date de début (YYYY-MM-DD)"),
    date_fin: Optional[str] = Query(None, description="Date de fin (YYYY-MM-DD)")
):
    # Créer une copie pour filtrer
    df_filtered = df.copy()

    # Filtrer par plage de dates si fournies
    if date_debut and date_fin:
        df_filtered = df_filtered[(df_filtered["Date"] >= date_debut) & (df_filtered["Date"] <= date_fin)]
    
    # Filtrer par service s'il est spécifié et reconnu
    if service and service in services_mapping:
        col = services_mapping[service]
        # Ne conserver que Date et la colonne du service, puis renommer en "Admissions"
        df_filtered = df_filtered[["Date", col]].rename(columns={col: "Admissions"})
        df_filtered["Admissions"] = pd.to_numeric(df_filtered["Admissions"], errors="coerce").fillna(0)
    else:
        # Sinon, utiliser la colonne Admissions_totales
        df_filtered = df_filtered[["Date", "Admissions_totales"]].rename(columns={"Admissions_totales": "Admissions"})
        df_filtered["Admissions"] = pd.to_numeric(df_filtered["Admissions"], errors="coerce").fillna(0)
    
    # Calcul du total des admissions sur la période filtrée
    total_admissions = df_filtered["Admissions"].sum()

    # Évolution des admissions par mois (agrégation mensuelle)
    evolution_admissions = df_filtered.groupby(df_filtered["Date"].dt.month)["Admissions"].sum().reset_index()
    evolution_list = evolution_admissions.to_dict(orient="records")
    
    # Calcul du temps d'attente moyen sur la période
    # Conversion en numérique pour la colonne de temps d'attente
    df["Temp_d’attente_moyen_minutes"] = pd.to_numeric(df["Temp_d’attente_moyen_minutes"], errors="coerce").fillna(0)
    df_temp = df[["Date", "Temp_d’attente_moyen_minutes"]]
    df_merged = pd.merge(df_filtered, df_temp, on="Date", how="left")
    temps_attente_moyen = df_merged["Temp_d’attente_moyen_minutes"].mean()
    
    # Répartition des admissions par jour de la semaine
    df_filtered["Jour"] = df_filtered["Date"].dt.day_name()
    admissions_par_jour = df_filtered.groupby("Jour")["Admissions"].sum().to_dict()
    
    return {
        "total_admissions": total_admissions,
        "evolution_admissions": evolution_list,
        "temps_attente_moyen": round(temps_attente_moyen, 2),
        "admissions_par_jour": admissions_par_jour
    }

@app.get("/admissions/repartition")
def get_admissions_repartition(
    date_debut: Optional[str] = Query(None, description="Date de début (YYYY-MM-DD)"),
    date_fin: Optional[str] = Query(None, description="Date de fin (YYYY-MM-DD)")
):
    # Filtrer par plage de dates si fourni
    df_filtered = df.copy()
    if date_debut and date_fin:
        df_filtered = df_filtered[(df_filtered["Date"] >= date_debut) & (df_filtered["Date"] <= date_fin)]
    
    repartition = {}
    for service, col in services_mapping.items():
        if col in df_filtered.columns:
            # Convertir en numérique, remplacer les erreurs par 0, sommer et convertir en int natif
            val = pd.to_numeric(df_filtered[col], errors="coerce").fillna(0).sum()
            repartition[service] = int(val)
        else:
            repartition[service] = 0
    
    return repartition

@app.get("/admissions/evolution")
def get_admissions_evolution(
    year: Optional[str] = Query(None, description="Année (ex: 2022)"),
    service: Optional[str] = Query(None, description="Service (ex: Neurologie)")
):
    # Copie du DataFrame
    df_filtered = df.copy()

    # Filtrer par année si précisée
    if year:
        df_filtered = df_filtered[df_filtered["Date"].dt.year == int(year)]

    # Choisir la colonne correspondant au service
    if service and service in services_mapping:
        col = services_mapping[service]
        # On s'assure que la colonne existe
        if col in df_filtered.columns:
            df_filtered["Admissions"] = pd.to_numeric(df_filtered[col], errors="coerce").fillna(0)
        else:
            # Colonne inexistante => 0
            df_filtered["Admissions"] = 0
    else:
        # Aucune sélection => "Admissions_totales"
        df_filtered["Admissions"] = df_filtered["Admissions_totales"]
    
    # Agrégation mensuelle
    evolution = (
        df_filtered.groupby(df_filtered["Date"].dt.month)["Admissions"]
        .sum()
        .reset_index()
        .rename(columns={"Date": "month", "Admissions": "admissions"})
    )

    # Convertir en int natif pour éviter les soucis de sérialisation
    evolution["admissions"] = evolution["admissions"].astype(int)

    # Convertir le DataFrame en liste de dictionnaires
    result = evolution.to_dict(orient="records")
    # Exemple de format : [ { "month": 1, "admissions": 12345 }, { "month": 2, ... } ]

    return result

@app.get("/admissions/distribution")
def get_admissions_distribution(
    year: Optional[str] = Query(None, description="Année (ex: 2022)"),
    service: Optional[str] = Query(None, description="Service (ex: Neurologie)")
):
    df_filtered = df.copy()

    # Filtrer par année
    if year:
        df_filtered = df_filtered[df_filtered["Date"].dt.year == int(year)]

    # Choisir la colonne pour le service
    if service and service in services_mapping:
        col = services_mapping[service]
        if col in df_filtered.columns:
            df_filtered["Admissions"] = pd.to_numeric(df_filtered[col], errors="coerce").fillna(0)
        else:
            df_filtered["Admissions"] = 0
    else:
        df_filtered["Admissions"] = df_filtered["Admissions_totales"]
    
    # Grouper par jour de la semaine
    df_filtered["weekday"] = df_filtered["Date"].dt.day_name()
    distribution = (
        df_filtered.groupby("weekday")["Admissions"]
        .sum()
        .reset_index()
        .rename(columns={"weekday": "day", "Admissions": "admissions"})
    )
    distribution["admissions"] = distribution["admissions"].astype(int)

    # Exemple de tri par ordre de la semaine (optionnel)
    # Lundi, Mardi, ...
    # On peut mapper day_name => index
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    distribution["day_index"] = distribution["day"].apply(lambda d: day_order.index(d) if d in day_order else 999)
    distribution = distribution.sort_values("day_index").drop(columns=["day_index"])

    result = distribution.to_dict(orient="records")
    # Exemple : [ { "day": "Monday", "admissions": 12345 }, { "day": "Tuesday", ... } ]

    return result
    
@app.get("/filters")
def get_filters():
    # Calcul de la plage de dates à partir du CSV
    min_date = df["Date"].min().date().isoformat()
    max_date = df["Date"].max().date().isoformat()

    return {
        "services": list(services_mapping.keys()),
        "date_range": {
            "min": min_date,
            "max": max_date
        }
    }
    
    
# Endpoint pour récupérer une prédiction basée sur l’algorithme
@app.get("/predictions")
def get_predictions():
    with open("predictions.json", "r") as f:
         predictions = json.load(f)
    return predictions

# Lancer le serveur API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    


