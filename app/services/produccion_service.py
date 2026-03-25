# Se define la logica del sistema (validar login, guardar produccion, buscar transformadores, etc.)

from app.config.database import db
from datetime import datetime
from bson import ObjectId

# REGISTRAR UNA PRODUCCION

def registrar_produccion(data, user):

    produccion = data.dict()

    # Validar transformador
    transformador = db.transformadores.find_one({
        "serial": produccion["transformador_serial"]
    })

    if not transformador:
        return {"error": "Transformador no existe"}

    # Validar ausencia
    hoy = datetime.now().strftime("%Y-%m-%d")

    ausencia = db.ausencias.find_one({
        "trabajador": produccion["trabajador"],
        "fecha_inicio": {"$lte": hoy},
        "fecha_fin": {"$gte": hoy}
    })

    if ausencia:
        return {"error": "El trabajador está ausente"}

    # Guardar usuario que hizo la acción
    produccion["usuario"] = user["usuario"]

    db.produccion.insert_one(produccion)

    return {"mensaje": "Producción registrada"}

def editar_produccion(id, datos):

    result = db.produccion.update_one({"_id": ObjectId(id)}, {"$set": datos})

    if result.modified_count == 0:
        return {"error": "No se pudo actualizara"}
    else:
        return {"mensaje": "Registro actualizado"}
    
def eliminar_produccion(id):

    result = db.produccion.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        return {"error": "No se pudo eliminar"}
    else:
        return {"mensaje": "Registro eliminado"}