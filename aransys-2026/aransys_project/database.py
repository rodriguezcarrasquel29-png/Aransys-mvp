from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Aquí le decimos a Python dónde está nuestra base de datos en Termux
DATABASE_URL = "sqlite:///./aransys.db" # Usaremos SQLite primero por ser más ligero en el cel

Base = declarative_base()

class RepuestoDB(Base):
    __tablename__ = "repuestos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    marca = Column(String)
    precio = Column(Float)
    anillo = Column(Integer) # Aquí guardaremos si es Anillo 1, 2, 3 o 4

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def crear_base_de_datos():
    Base.metadata.create_all(bind=engine)
