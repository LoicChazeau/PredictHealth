from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

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

latest_data = df.iloc[-1]  # Aujourd’hui
yesterday_data = df.iloc[-2]  # Hier

# Endpoint pour récupérer toutes les données
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

# Endpoint pour récupérer les données du dashboard
@app.get("/dashboard")
def get_dashboard():
    # 🔹 Admissions Totales
    admissions_jour = int(latest_data["Admissions_totales"])
    admissions_hier = int(yesterday_data["Admissions_totales"]) if not yesterday_data.empty else admissions_jour

    # 🔹 Évolution Admissions (%)
    evolution_admissions = (
        round(((admissions_jour - admissions_hier) / admissions_hier) * 100, 2)
        if admissions_hier != 0 else 0
    )

    # 🔹 Taux d’occupation des lits
    taux_occupation = round(
        (latest_data["Lits_occupes"] / (latest_data["Lits_disponibles"] + latest_data["Lits_occupes"])) * 100, 2
    )
    taux_occupation_hier = round(
        (yesterday_data["Lits_occupes"] / (yesterday_data["Lits_disponibles"] + yesterday_data["Lits_occupes"])) * 100, 2
    ) if not yesterday_data.empty else taux_occupation

    evolution_taux_occupation = round(taux_occupation - taux_occupation_hier, 2)

    # 🔹 Temps d’attente moyen
    temps_attente_jour = int(latest_data["Temp_d’attente_moyen_minutes"])
    temps_attente_hier = int(yesterday_data["Temp_d’attente_moyen_minutes"]) if not yesterday_data.empty else temps_attente_jour

    evolution_temps_attente = (
        round(((temps_attente_jour - temps_attente_hier) / temps_attente_hier) * 100, 2)
        if temps_attente_hier != 0 else 0
    )

    return {
        "admissions_jour": admissions_jour,
        "evolution_admissions": f"{evolution_admissions}%",
        "taux_occupation": f"{taux_occupation}%",
        "evolution_taux_occupation": f"{evolution_taux_occupation}%",
        "temps_attente_jour": f"{temps_attente_jour} min",
        "evolution_temps_attente": f"{evolution_temps_attente}%",
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
