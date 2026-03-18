from app.config.database import db
from app.utils.security import hash_password

admin = {
    "nombre": "Administrador",
    "usuario": 1025520831,
    "password": hash_password("123456"),
    "rol": "admin"
}

# Verificar si ya existe
if db.usuarios.find_one({"usuario": "admin"}):
    print("El usuario admin ya existe")
else:
    db.usuarios.insert_one(admin)
    print("Usuario admin creado correctamente")     