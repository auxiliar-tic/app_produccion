# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db
from app.utils.dependencies import get_current_user, Depends
from fastapi import HTTPException

# CREAR TRANSFORMADOR EN LA BASE DE DATOS

def crear_transformador(data):

    trnasformador = data.dict() #convertir el modelo en diccionario

    #validar si existe el transformador 
    existente = db.transformadores.find_one({"serial": trnasformador["serial"]})

    if existente:
        return {"error": "El transformador ya existe"}

    db.transformadores.insert_one(trnasformador) #guardar en la base de datos

    return {"mensaje": "Transformador creado"}

# LISTAR LOS TRANSFORMADORES DE LA BASE DE DATOS

def listar_transformadores():
    data = list(db.transformadores.find())

    for item in data:
        item["_id"] = str(item["_id"])  # 🔥 CLAVE

    return data

# BUSCAR TRANSFORMADORES EN LA BASE DE DATOS 

#BUSCAR POR SERIAL EL TRANSFORMADOR
def buscar_transformador(serial):

    transformador = db.transformadores.find_one({"serial": serial})

    if not transformador:
        return {"error": "Transformador no encontrado"}

    transformador["_id"] = str(transformador["_id"])

    return transformador
