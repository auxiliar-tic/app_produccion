# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter, Depends
from app.models.produccion_model import Produccion
from app.services import produccion_service
from app.utils.dependencies import get_current_user
from app.config.database import db
from bson import ObjectId

router = APIRouter(prefix="/produccion")

@router.post("/")
def registrar(
    data: Produccion,
    user = Depends(get_current_user) #solo usuarios con token pueden registrar
    ):
    return produccion_service.registrar_produccion(data,user)

from bson import ObjectId

@router.put("/{id}")
def actualizar(id: str, data: dict, user=Depends(get_current_user)):

    db.produccion.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )

    return {"msg": "Actualizado"}

@router.delete("/{id}")
def eliminar(id:str, user = Depends(get_current_user)):
    return produccion_service.eliminar_produccion(id)