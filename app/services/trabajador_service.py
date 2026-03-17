# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db

def crear_trabajador(data):

    trabajador = data.dict() #convertir el modelo en diccionario

    existe = db.trabajadores.find_one({"nombre": trabajador["nombre"]})

    if existe:
        return {"error": "El trabajador ya existe"}

    db.trabajadores.insert_one(trabajador) #guardar en la base de datos

    return {"mensaje": "Trabajador creado"}

def obtener_trabajadores():
    return list(db.trabajadores.find({}, {"_id": 0}))