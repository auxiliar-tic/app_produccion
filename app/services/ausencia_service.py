# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)


from app. config.database import db

def registrar_ausencia(data):

    ausencia = data.dict() #convertir el modelo en diccionario

    db.ausencias.insert_one(ausencia) #guardar en la base de datos

    return {"mensaje": "Ausencia creada"}