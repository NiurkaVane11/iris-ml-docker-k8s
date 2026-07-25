from fastapi import FastAPI
import joblib
import numpy as np

# Crear API
app = FastAPI()

# Cargar modelo entrenado
model = joblib.load("model.pkl")


@app.get("/")
def home():
    return {"mensaje": "API Iris funcionando"}


@app.post("/predict")
def predict(features: list[float]):

    # Convertir entrada a formato esperado por sklearn
    data = np.array(features).reshape(1, -1)

    # Realizar predicción
    prediction = model.predict(data)

    return {
        "class": int(prediction[0])
    }