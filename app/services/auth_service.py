# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db
from app.utils.security import verify_password, create_token

def login(usuario, password):

    user = db.usuarios.find_one({"usuario": usuario})

    if not user:
        return {"error": "Usuario no encontrado"}

    if not verify_password(password, user.get("password", "")):
        return {"error": "Contraseña incorrecta"}

    rol = user.get("rol")
    if not rol:
        rol = "user"  # Valor por defecto si no está definido en el documento

    token = create_token({
        "usuario": user.get("usuario", usuario),
        "rol": rol
    })

    return {
        "token": token,
        "name": user.get("nombre", ""),
        "rol": rol
    }