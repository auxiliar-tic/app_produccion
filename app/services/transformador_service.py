# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db

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

    transformadores = list(db.transformadores.find({},{"_id": 0}))

    return transformadores

# BUSCAR TRANSFORMADORES EN LA BASE DE DATOS 

def buscar_transformador(serial):

    transformador = db.transformadores.find_one(
        {"serial": serial},
        {"_id": 0}
    )

    if not transformador:
        return {"error": "Transformador no encontrado"}

    return transformador