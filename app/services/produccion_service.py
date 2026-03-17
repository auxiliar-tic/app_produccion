# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db

# REGISTRAR UNA PRODUCCION
def registrar_produccion(data):

    produccion = data.dict() #convertir el modelo en diccionario
    
    #validar que el transformado exista
    transformador = db.transformadores.find_one({
        "serial": produccion["trnasformador_serial"]
        })
    
    if not transformador:
        return {"error": "El transformador no existe"}
    
    db.produccion.insert_one(produccion) #guardar en la base de datos

    return {"mensaje": "Produccion creada"}