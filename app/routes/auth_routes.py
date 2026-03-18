# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter
from app.services.auth_service import login
from app.models.auth_model import Login

router = APIRouter()

@router.post("/login")
def login_user(data: Login):
    return login(data.usuario, data.password)