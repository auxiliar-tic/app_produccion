from app.config.database import db

#Obtener la produccion
def obtener_produccion():

    data = list(db.produccion.find())

    for item in data:

        item["_id"] = str(item["_id"])

        # 👤 usuario
        usuario = item.get("usuario")
        user = db.usuarios.find_one({"usuario": usuario})
        item["nombre"] = user["nombre"] if user else "Sin usuario"

        # 🔌 transformador
        serial = item.get("transformador_serial")
        trans = db.transformadores.find_one({"serial": serial})

        if trans:
            item["serial"] = trans.get("serial")
            item["potencia"] = trans.get("potencia")
            item["voltaje"] = trans.get("voltaje")
            item["cliente"] = trans.get("cliente")
            item["lote"] = trans.get("lote")
            item["fase"] = trans.get("fase")
        else:
            item["serial"] = "N/A"
            item["potencia"] = ""
            item["voltaje"] = ""
            item["cliente"] = ""
            item["lote"] = ""
            item["fase"] = ""

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