from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"status": "ARansys Online", "ciudad": "Maturin"}

@app.post("/repuestos/", response_model=schemas.RepuestoResponse)
def crear_repuesto(repuesto: schemas.RepuestoCreate, db: Session = Depends(get_db)):
    nuevo_db = models.RepuestoTabla(
        nombre=repuesto.nombre,
        marca=repuesto.marca,
        modelo_carro=repuesto.modelo_carro,
        precio=repuesto.precio,
        anillo=repuesto.anillo
    )
    db.add(nuevo_db)
    db.commit()
    db.refresh(nuevo_db)
    return nuevo_db

@app.get("/repuestos/")
def listar_repuestos(db: Session = Depends(get_db)):
    return db.query(models.RepuestoTabla).all()
