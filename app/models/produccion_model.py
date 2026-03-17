# Este archivo define la estructura de los datos, que campos tendra cada objeto

from pydantic import BaseModel

class Produccion(BaseModel):
    trabajador: str
    trnasformador_serial: str
    proceso: str
    descripcion: str
    fecha :str