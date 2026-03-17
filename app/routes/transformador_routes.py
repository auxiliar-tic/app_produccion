# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter
from app.models.transformador_model import Transformador
from app.services import transformador_service

router = APIRouter(prefix="/transformadores")

#CREAR TRANSFORMADOR
@router.post("/")
def crear(data: Transformador):
    return transformador_service.crear_transformador(data)

#LISTAR LOS TRANSFORMDORES
@router.get("/")
def listar():
    return transformador_service.listar_transformadores()

#BUSCAR POR SERIAL EL TRANSFORMADOR
@router.get("/{serial}")
def buscar(serial: str):
    return transformador_service.buscar_transformador(serial)