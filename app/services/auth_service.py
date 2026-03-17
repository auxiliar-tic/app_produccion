# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db
from app.utils.security import verify_password, create_token

def login(usuario, password):

    user = db.usuarios.find_one({"username": usuario})

    if not user:
        return {"error": "Usuario no encontrado"}
    
    if not verify_password(password, user["password"]):
        return {"error": "Contraseña incorrecta"}
    
    token = create_token({
        "username": user["username"]
        })

    return {"token": token}