"""
Direcciones API OAuth2
"""
from fastapi import FastAPI

# from datetime import timedelta
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session

from fastapi_pagination import add_pagination

# from config.settings import ACCESS_TOKEN_EXPIRE_MINUTES
# from lib.database import get_db

# from plataforma_web.v1.usuarios.authentications import authenticate_user, create_access_token, get_current_active_user
# from plataforma_web.v1.usuarios.schemas import Token, UsuarioInBD


app = FastAPI(
    title="Direcciones API OAuth2",
    description="API de Direcciones",
)

add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a Direcciones API OAuth2 del Poder Judicial del Estado de Coahuila de Zaragoza."}
