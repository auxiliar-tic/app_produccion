from reportlab.platypus import SimpleDocTemplate,Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from app.config.database import db

def generar_pdf_historial(serial):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    elementos = []

    styles = getSampleStyleSheet()

    #Titulo
    titulo = Paragraph(f"Historial del transformador {serial}", styles["Title"])
    elementos.append(titulo)

    #Obtener datos
    data = list(db.produccion.find(
        {"transformador_serial":serial},
        {"_id":0}
    ))

    #ordenar por fecha
    data.sort(key=lambda x: x["fecha"])

    #Encabezados de tabla
    tabla_data = [["Fecha", "Proceso","Usuario"]]

    #llenar tabla
    for item in data:

        usuario = item.get("usuario")

        if usuario:
            user = db.usuarios.find_one({"usuario": usuario})
            nombre = user["nombre"] if user else "Desconocido"
        else:
            nombre = "Sin usuario"

        tabla_data.append([
            item.get("fecha",""),
            item.get("proceso",""),
            nombre
        ])

    #crear tabla
    tabla = Table(tabla_data)

    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elementos.append(tabla)

    #construir PDF
    doc.build(elementos)

    buffer.seek(0)

    return buffer