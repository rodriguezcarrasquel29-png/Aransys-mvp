from fastapi import FastAPI

# Creamos la aplicación (El motor)
app = FastAPI()

# Esto es una "Ruta". 
# Es lo que pasa cuando alguien entra a la dirección principal de tu web.
@app.get("/")
def inicio():
    return {"mensaje": "Motor ARansys encendido y listo en Maturín"}

# Esta es la ruta para ver los repuestos
@app.get("/repuestos")
def lista_repuestos():
    # Por ahora, devolvemos una lista de prueba (como un inventario en papel)
    return [
        {"id": 1, "nombre": "Actuador Whirlpool", "precio": 45},
        {"id": 2, "nombre": "Bomba de agua LG", "precio": 20}
    ]
