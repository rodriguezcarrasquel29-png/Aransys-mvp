from sqlalchemy import Column, Integer, String, Float
from database import Base

class RepuestoTabla(Base):
    __tablename__ = "repuestos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    marca = Column(String)
    modelo_carro = Column(String)
    precio = Column(Float)
    anillo = Column(Integer)
