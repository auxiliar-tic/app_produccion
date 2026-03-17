# archivo de inicio donde ejecutamos uvicorn app.main:app --reload para iniciar el servidor

from fastapi import FastAPI
from app.routes import auth_routes

app = FastAPI()

app.include_router(auth_routes.router)

@app.get("/")
def home():
    return {"mensaje":"API Funcionando"}