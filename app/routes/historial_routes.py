# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter, Depends
from app.services import historial_service
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/historial")

# Cualquier usuario puede ver el historial de un transformador concreto

@router.get("/transformador/{serial}")
def obtener_historial(
    serial: str,
    user: dict = Depends(get_current_user)
    ):

    return historial_service.historial_transformador(serial)
