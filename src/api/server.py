from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

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


# Endpoint pour récupérer une prédiction basée sur l’algorithme
@app.get("/predict/{date}")
def predict(date: str):
    # ICI, APPELER LA FONCTION D’ANALYSE PREDICTIVE DU NOTEBOOK
    prediction = {
        "date": date,
        "prediction": 125
    }
    return prediction

# Lancer le serveur API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    


