# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter
from app.models.produccion_model import Produccion
from app.services import produccion_service

router = APIRouter(prefix="/produccion")

@router.post("/")
def registrar(data: Produccion):
    return produccion_service.registrar_produccion(data)