# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter, Depends
from app.models.proceso_model import Proceso
from app.services import proceso_service
from app.utils.dependencies import require_role, get_current_user
from app.config.database import db

router = APIRouter(prefix="/procesos")

@router.post("/")
def crear(data: Proceso,
        user = Depends(require_role("admin"))
        ):
    return proceso_service.crear_proceso(data,user)

@router.get("/")
def listar_procesos(user=Depends(get_current_user)):
    return proceso_service.obtener_procesos()