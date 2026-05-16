from pydantic import BaseModel

class RepuestoBase(BaseModel):
    nombre: str
    marca: str
    modelo_carro: str
    precio: float
    anillo: int

class RepuestoCreate(RepuestoBase):
    pass

class RepuestoResponse(RepuestoBase):
    id: int
    class Config:
        from_attributes = True
        orm_mode = True
