# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter, Depends
from app.models.transformador_model import Transformador
from app.services import transformador_service
from app.utils.dependencies import require_role
from app.config.database import db

router = APIRouter(prefix="/transformadores")

#CREAR TRANSFORMADOR
@router.post("/")
def crear_transformador(data: dict, user=Depends(require_role("admin"))):

    db.transformadores.insert_one(data)

    return {"msg": "Transformador creado"}

#LISTAR LOS TRANSFORMDORES
@router.get("/")
def listar():
    return transformador_service.listar_transformadores()

#BUSCAR POR SERIAL EL TRANSFORMADOR
@router.get("/{serial}")
def buscar(serial: str):
    return transformador_service.buscar_transformador(serial)

@router.put("/{id}")
def actualizar_transformador(id: str, data: dict, user=Depends(require_role("admin"))):

    from bson import ObjectId

    db.transformadores.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )

    return {"msg": "Transformador actualizado"}


@router.delete("/{serial}")
def eliminar(serial: str, user=Depends(require_role("admin"))):
    db.transformadores.delete_one({"serial": serial})
    return {"msg": "Eliminado"}