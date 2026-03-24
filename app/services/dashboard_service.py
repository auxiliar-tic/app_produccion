# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db

#agrupar por fecha,  cuenta de registros ,ordenar
def produccion_por_dia():

    pipeline = [
        {
            "$group": {
                "_id":"$fecha",
                "total":{"$sum": 1}

                }
            },
        {
            "$sort": {"_id": -1}}
        ]

    return list(db.produccion.aggregate(pipeline))


# Ranking de trabajadores, mas productivo de primeras
def produccion_por_usuario():

    pipeline = [
        {
            "$group": {
                "_id":"$usuario",
                "total":{"$sum": 1}

                }
            },
        {
            "$sort": {"_id": -1}}
        ]
        
    data = list(db.produccion.aggregate(pipeline))
        
        #agregar nombre de usuario
    for item in data:

            usuario = item.get("_id")

            if usuario:
                user = db.usuarios.find_one({"usuario": usuario})
                item["nombre"] = user["nombre"] if user else "Desconocido"
            else:
                item["nombre"] = "Sin usuario"

    return data


#procesos mas usados
def procesos_mas_usados():

    pipeline = [
        {
            "$group": {
                "_id":"$proceso",
                "total":{"$sum": 1}

                }
            },
        {
            "$sort": {"_id": -1}}
        ]

    return list(db.produccion.aggregate(pipeline))


#produccion por transformador
def produccion_por_transformador():

    pipeline = [
        {
            "$group": {
                "_id":"$transformador_serial",
                "total":{"$sum": 1}

                }
            },
        {
            "$sort": {"_id": -1}}
        ]

    return list(db.produccion.aggregate(pipeline))
            