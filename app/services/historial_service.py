# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

#se define la historia completa del transformador (filtrar por serial, ordenar por fecha, nombre de usuario)

from app.config.database import db

def historial_transformador(serial):

    #buscar todos los registros de ese transformador
    data = list(db.produccion.find(
        {"transformador_serial":serial},
        {"_id":0}
        ))
    
    #ordenar por fecha
    data.sort(key=lambda x: x["fecha"])

    #agregar nombre del usuario
    for item in data:

        usuario = item.get("usuario")

        if usuario:
            user = db.usuarios.find_one({"usuario": usuario})
            item["nombre"] = user["nombre"] if user else "Desconocido"
        else:
            item["nombre"] = "Sin usuario"

    return data