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

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}
