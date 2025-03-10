from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Charger les données
df = pd.read_csv("src/api/Global_dataset.csv")

# Endpoint pour récupérer toutes les données
@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

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
