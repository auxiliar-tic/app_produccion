# Este archivo define la estructura de los datos, que campos tendra cada objeto

from pydantic import BaseModel

class Usuario(BaseModel):
    username: str
    password: str
    role: str