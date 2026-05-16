from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, database

# Creamos las tablas en el celular
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Función para calcular el flete en Maturín
def calcular_flete(distancia_km):
    if distancia_km <= 3: return 1  # Anillo 1
    elif distancia_km <= 7: return 2 # Anillo 2
    elif distancia_km <= 15: return 3 # Anillo 3
    else: return 4 # Anillo 4

@app.get("/")
def inicio():
    return {"mensaje": "ARansys Maturín 2026 - Sistema de Repuestos"}

# Ruta para calcular envío rápidamente
@app.get("/cotizar/{distancia}")
def cotizar(distancia: float):
    anillo = calcular_flete(distancia)
    return {"distancia": distancia, "anillo": anillo, "costo_estimado": f"Zona {anillo}"}

