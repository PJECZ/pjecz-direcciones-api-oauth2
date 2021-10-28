"""
Direcciones API OAuth2
"""
from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from fastapi_pagination import add_pagination

from config.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from lib.database import get_db

from direcciones.v1.codigos_postales.paths import codigos_postales
from direcciones.v1.estados.paths import estados
from direcciones.v1.municipios.paths import municipios
from direcciones.v1.roles.paths import roles
from direcciones.v1.usuarios.paths import usuarios

from direcciones.v1.usuarios.authentications import authenticate_user, create_access_token, get_current_active_user
from direcciones.v1.usuarios.schemas import Token, UsuarioInBD


app = FastAPI(
    title="Direcciones API OAuth2",
    description="API de Direcciones",
)

app.include_router(roles)
app.include_router(usuarios)
app.include_router(estados)
app.include_router(municipios)
app.include_router(codigos_postales)

add_pagination(app)


@app.get("/")
async def root():
    """Mensaje de Bienvenida"""
    return {"message": "Bienvenido a Direcciones API OAuth2 del Poder Judicial del Estado de Coahuila de Zaragoza."}


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Entregar el token como un JSON"""
    usuario = authenticate_user(form_data.username, form_data.password, db)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": usuario.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/usuarios/yo/", response_model=UsuarioInBD)
async def read_users_me(current_user: UsuarioInBD = Depends(get_current_active_user)):
    """Mostrar el perfil del usuario"""
    return current_user
