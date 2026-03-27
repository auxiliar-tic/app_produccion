from app.config.database import db

#Obtener la produccion
def obtener_produccion():

    data = list(db.produccion.find())

    for item in data:

        # 🔥 convertir _id
        item["_id"] = str(item["_id"])

        usuario = item.get("usuario")

        if usuario:
            user = db.usuarios.find_one({"usuario": usuario})
            item["nombre"] = user["nombre"] if user else "Desconocido"
        else:
            item["nombre"] = "Sin usuario"

    return data


# Filtar por usuario
def produccion_por_usuario(usuario):

    data = list(db.produccion.find(
        {"usuario":usuario}
    ))

    for item in data:

        item["_id"] = str(item["_id"])

        usuario = item.get("usuario")

        if usuario:
            user = db.usuarios.find_one({"usuario": usuario})
            item["nombre"] = user["nombre"] if user else "Desconocido"
        else:
            item["nombre"] = "Sin usuario"

    return data


#Filtar por fecha 
def produccion_por_fecha(fecha):

    data = list(db.produccion.find(
        {"fecha":fecha},
    ))

    for item in data:

        item["_id"] = str(item["_id"])

        usuario = item.get("usuario")

        if usuario:
            user = db.usuarios.find_one({"usuario": usuario})
            item["nombre"] = user["nombre"] if user else "Desconocido"
        else:
            item["nombre"] = "Sin usuario"

    return data