# archivo de inicio donde ejecutamos uvicorn app.main:app --reload para iniciar el servidor

from fastapi import FastAPI
from app.routes import auth_routes, trabajador_routes, ausencia_routes
from app.routes import transformador_routes, usuario_routes
from app.routes import produccion_routes, proceso_routes

app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(transformador_routes.router)
app.include_router(produccion_routes.router)
app.include_router(proceso_routes.router)
app.include_router(trabajador_routes.router)
app.include_router(ausencia_routes.router)
app.include_router(usuario_routes.router)

@app.get("/")
def home():
    return {"mensaje":"API Funcionando"}

