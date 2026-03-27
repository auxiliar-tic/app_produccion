# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db

def crear_proceso(data):

    proceso = data.dict() #convertir el modelo en diccionario
    
    #validar si existe el proceso
    existe = db.procesos.find_one({"nombre": proceso["nombre"]})

    if existe:
        return {"error": "El proceso ya existe"}

    db.procesos.insert_one(proceso) #guardar en la base de datos

    return {"mensaje": "Proceso creado"}

def obtener_procesos():
        data = list(db.procesos.find())

        for item in data:
            item["_id"] = str(item["_id"])

        return data
