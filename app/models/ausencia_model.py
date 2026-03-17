# Este archivo define la estructura de los datos, que campos tendra cada objeto

from pydantic import BaseModel

class Ausencia(BaseModel):
    trabajador: str
    fecha_inicio : str
    fecha_fin : str
    motivo : str