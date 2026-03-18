from pydantic import BaseModel

class Login(BaseModel):
    usuario: int
    password: str