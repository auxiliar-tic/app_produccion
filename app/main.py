# archivo de inicio donde ejecutamos uvicorn app.main:app --reload para iniciar el servidor

from fastapi import FastAPI
from app.config.database import db

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}