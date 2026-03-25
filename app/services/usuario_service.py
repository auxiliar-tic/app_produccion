# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

#CODIGO PARA QUE EL ADMIN PUEDA CREAR USUARIOS Y LISTARLOS, SOLO EL ADMIN PUEDE HACER ESTO
from app.config.database import db
from app.utils.security import hash_password
from bson import ObjectId

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

def editar_usuarios(id, datos):

    if "password" in datos:
        from app.utils.security import hash_password
        datos ["password"] = hash_password(datos["password"])

    result = db.usuarios.update_one({"_id": ObjectId(id)}, {"$set": datos})

    if result.modified_count == 0:
        return {"error": "No se pudo actualizar"}
    
    return {"mensaje": "Registro actualizado"}

def eliminar_usuarios(id):

    result = db.usuarios.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        return {"error": "No se pudo eliminar"}
    
    return {"mensaje": "Registro eliminado"}