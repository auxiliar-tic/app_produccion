# validar permisos, encriptar contraseñas, generar tokens

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str): #encriptar la contraseña 
    return pwd_context.hash(password)  

def verify_password(plain_password: str, hashed_password: str): #verificar la contraseña
    return pwd_context.verify(plain_password, hashed_password) 

def create_token(data: dict):  #crear token 
    expire = datetime.utcnow() + timedelta(hours=8)

    data.update({"exp": expire})

    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)