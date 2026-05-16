from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Repuesto(Base):
    __tablename__ = "inventario_aransys"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    marca = Column(String)
    modelo_carro = Column(String)
    precio = Column(Float)
    anillo = Column(Integer)  # Para la logística de Maturín
    disponible = Column(Boolean, default=True)
