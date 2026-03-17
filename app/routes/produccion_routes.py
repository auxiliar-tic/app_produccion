# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter, Depends
from app.models.produccion_model import Produccion
from app.services import produccion_service
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/produccion")

@router.post("/")
def registrar(
    data: Produccion,
    user = Depends(get_current_user) #solo usuarios con token pueden registrar
    ):
    return produccion_service.registrar_produccion(data,user)