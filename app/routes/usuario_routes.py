#se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

#CODIGO PARA QUE EL ADMIN PUEDA CREAR USUARIOS Y LISTARLOS, SOLO EL ADMIN PUEDE HACER ESTO

from fastapi import APIRouter, Depends
from app.models.usuario_model import Usuario
from app.services import usuario_service
from app.utils.dependencies import require_role

router = APIRouter(prefix="/usuarios")

#CREAR USUARIO (solo admin)
@router.post("/")
def crear(
    data: Usuario,
    user = Depends(require_role("admin")) #solo usuarios con token pueden registrar
):
    return usuario_service.crear_usuario(data)

#LISTAR USUARIOS (solo admin)
@router.get("/listar")
def listar(
        user = Depends(require_role("admin")) #solo usuarios con token pueden registrar
    ): 
    return usuario_service.obtener_usuarios()

@router.put("/{id}")
def actualizar_usuario(id:str, datos: dict, user = Depends(require_role("admin"))):
    return usuario_service.editar_usuarios(id,datos)

@router.delete("/{id}")
def eliminar_usuario(id:str, user = Depends(require_role("admin"))):        
    return usuario_service.eliminar_usuarios(id)