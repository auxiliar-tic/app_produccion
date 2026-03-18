# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db
from app.utils.security import hash_password

# crear usuarios en el sistema

def crear_usuario(data):

    usuario = data.dict() #convertir el modelo en diccionario

    #validar si existe el usuario
    existe = db.usuarios.find_one({"usuario": usuario["usuario"]})

    if existe:
        return {"error": "El usuario ya existe"}

    usuario["password"] = hash_password(usuario["password"]) #encriptar la contraseña

    db.usuarios.insert_one(usuario) #guardar en la base de datos

    return {"mensaje": "Usuario creado Correctamente"}

# Listar usuarios

def obtener_usuarios():
    return list(db.usuarios.find({}, {"_id": 0, "password": 0})) #password:0 se oculta la contraseña