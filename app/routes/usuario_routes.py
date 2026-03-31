#se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

#CODIGO PARA QUE EL ADMIN PUEDA CREAR USUARIOS Y LISTARLOS, SOLO EL ADMIN PUEDE HACER ESTO

from fastapi import APIRouter, Depends
from app.models.usuario_model import Usuario
from app.services import usuario_service
from app.utils.dependencies import require_role
from app.config.database import db
from app.utils.security import hash_password

router = APIRouter(prefix="/usuarios")

#CREAR USUARIO (solo admin)
@router.post("/")
def crear_usuario(data: dict, user=Depends(require_role("admin"))):

    from app.utils.security import hash_password

    data["password"] = hash_password(data["password"])

    db.usuarios.insert_one(data)

    return {"msg": "Usuario creado"}

#LISTAR USUARIOS (solo admin)
@router.get("/")
def listar(
        user = Depends(require_role("admin")) #solo usuarios con token pueden registrar
    ): 
    return usuario_service.obtener_usuarios()

@router.put("/{usuario}")
def actualizar(usuario: int, data: dict, user = Depends(require_role("admin"))):

    update_data = {
        "nombre": data.get("nombre"),
        "rol": data.get("rol"),
        "usuario": data.get("usuario")
    }

    if "password" in data:
        update_data["password"] = hash_password(data["password"])

    result = db.usuarios.update_one(
        {"usuario": usuario},
        {"$set": update_data}
    )

    print("MARCHED: ", result.matched_count)
    print("MODIFIED: ", result.matched_count)

    if result.modified_count == 0:
        return {"error": "No se pudo actualizar"}

    return {"msg": "Usuario actualizado"}

@router.delete("/{usuario}")
def eliminar_usuario(usuario: int, user = Depends(require_role("admin"))):

    db.usuarios.delete_one({"usuario": usuario})

    return {"msg": "Usuario eliminado"}