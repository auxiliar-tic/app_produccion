# Configuracion del sistema (conexion a la base de datos, variables del servidor, etc.)

from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

#Obtener variables
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

#Crear cliente de MongoDB
client = MongoClient(MONGO_URI)

# Seleccionar base de datos
db = client[DATABASE_NAME]