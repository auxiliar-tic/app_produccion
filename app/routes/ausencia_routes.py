# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter, Depends
from app.models.ausencia_model import Ausencia
from app.services import ausencia_service
from app.utils.dependencies import require_role

router = APIRouter(prefix="/ausencias")

@router.post("/")
def crear(
    data: Ausencia,
    user = Depends(require_role("admin")) #solo usuarios con token pueden registrar
    ):
    return ausencia_service.registrar_ausencia(data)