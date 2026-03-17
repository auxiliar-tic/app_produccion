# Este archivo define la estructura de los datos, que campos tendra cada objeto

from pydantic import BaseModel

class Trabajador(BaseModel):
    nombre: str
    cargo: str
    estado: str #activo / inactivo