from fastapi import APIRouter, Depends
from app.services import dashboard_service
from app.utils.dependencies import require_role

router = APIRouter(prefix="/dashboard") 

# solo ADMIN


@router.get("/produccion_dia")
def procesos_dia(user = Depends(require_role("admin"))):
    return dashboard_service.produccion_por_dia()

@router.get("/produccion_usuario")
def procesos_usuario(user = Depends(require_role("admin"))):
    return dashboard_service.produccion_por_usuario()

@router.get("/procesos")
def procesos(user = Depends(require_role("admin"))):
    return dashboard_service.procesos_mas_usados()

@router.get("/transformadores")
def transformadores(user=Depends(require_role("admin"))):
    return dashboard_service.produccion_por_transformador()