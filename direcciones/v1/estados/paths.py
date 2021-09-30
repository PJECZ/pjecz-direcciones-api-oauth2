"""
Estados v1, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from direcciones.v1.roles.models import Permiso
from direcciones.v1.usuarios.authentications import get_current_active_user
from direcciones.v1.usuarios.schemas import UsuarioInBD

from direcciones.v1.estados.crud import get_estados, get_estado
from direcciones.v1.estados.schemas import EstadoOut

estados = APIRouter(prefix="/v1/estados", tags=["estados"])


@estados.get("", response_model=LimitOffsetPage[EstadoOut])
async def list_paginate(
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Listado de estados"""
    if not current_user.permissions & Permiso.VER_CUENTAS == Permiso.VER_CUENTAS:
        raise HTTPException(status_code=403, detail="Forbidden")
    return paginate(get_estados(db))


@estados.get("/{estado_id}", response_model=EstadoOut)
async def detail(
    estado_id: int,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de una estado a partir de su id"""
    if not current_user.permissions & Permiso.VER_CUENTAS == Permiso.VER_CUENTAS:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        estado = get_estado(db, estado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return EstadoOut.from_orm(estado)
