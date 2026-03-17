# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db

# REGISTRAR UNA PRODUCCION
def registrar_produccion(data, user):

    produccion = data.dict() #convertir el modelo en diccionario
    
    produccion["username"] = user["username"]

    db.producciones.insert_one(produccion) #guardar en la base de datos

    return {"mensaje": "Produccion creada"}