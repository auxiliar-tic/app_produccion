# En este archivo se controla a lo que el usuario puede acceder 

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

security = HTTPBearer()

#VERIFICAR TOKEN DE ACCESO

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Token Invalido")
    
# VALIDACION DE ROLES
    
def require_role(rol_requerido: str):

    def role_checker(user = Depends(get_current_user)):
        if user["rol"] != rol_requerido: 
            raise HTTPException(status_code=403, detail="Acceso Denegado")
        return user
    return role_checker