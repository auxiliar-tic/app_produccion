# Este archivo define la estructura de los datos, que campos tendra cada objeto

from pydantic import BaseModel

class Transformador(BaseModel):
    serial : str
    cliente : str
    marca : str
    potencia : int
    voltaje : str
    lote : int
    numero : int
    fase : int 
    servicio : str