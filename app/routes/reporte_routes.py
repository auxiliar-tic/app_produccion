from fastapi import APIRouter, Depends
from app.services import reporte_service
from app.utils.dependencies import require_role

router = APIRouter(prefix="/reportes")

# solo ADMIN 

#ver todo
@router.get("/")
def obtener_todos(user = Depends(require_role("admin"))):
    return reporte_service.obtener_produccion()

#filtrar por usuario
@router.get("/usuario/{usuario}")
def por_usuario(usuario: int, user = Depends(require_role("admin"))):
    return reporte_service.produccion_por_usuario(usuario)

# filtrar por fecha 
@router.get("/fecha/{fecha}")
def por_fecha(fecha: str, user = Depends(require_role("admin"))):
    return reporte_service.produccion_por_fecha(fecha)