from openpyxl import Workbook
from io import BytesIO
from app.config.database import db  

def generar_excel_historial(serial):

    wb = Workbook()
    ws = wb.active
    ws.title = "Historial"

    # Encabezados de la tabla
    ws.append(["Fecha", "Proceso", "Usuario"])

    #Obtener datos
    data = list(db.produccion.find(
        {"transformador_serial":serial},
        {"_id":0}
    ))

    #Ordenar por fecha
    data.sort(key=lambda x: x["fecha"])

     # Llenar datos
    for item in data:

        usuario = item.get("usuario")

        if usuario:
            user = db.usuarios.find_one({"usuario": usuario})
            nombre = user["nombre"] if user else "Desconocido"
        else:
            nombre = "Sin usuario"

        ws.append([
            item.get("fecha", ""),
            item.get("proceso", ""),
            nombre
        ])

    # Guardar en memoria
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    return buffer