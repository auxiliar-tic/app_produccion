# se definen los endpoints que el frontend usara (POST /login GET /transformadores POST /produccion)

from fastapi import APIRouter
from app.services.auth_service import login

router = APIRouter()

@router.post("/login")
def login_user(data: dict):

    username = data.get("username")
    password = data.get("password")

    return login(username, password)