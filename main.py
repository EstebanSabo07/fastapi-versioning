from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista temporal para almacenar usuarios
users = []

# Modelo de datos para un usuario
class User(BaseModel):
    id: int
    name: str
    email: str

# Endpoint POST para agregar un usuario
@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}

# Endpoint GET para obtener la lista de usuarios
@app.get("/users/")
async def get_users():
    return {"users": users}
