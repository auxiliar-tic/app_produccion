# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter
from app.models.proceso_model import Proceso
from app.services import proceso_service

router = APIRouter(prefix="/procesos")

@router.post("/")
def crear(data: Proceso):
    return proceso_service.crear_proceso(data)

@router.get("/")
def listar():
    return proceso_service.obtener_procesos()