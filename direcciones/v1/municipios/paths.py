"""
Municipios v1, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from direcciones.v1.roles.models import Permiso
from direcciones.v1.usuarios.authentications import get_current_active_user
from direcciones.v1.usuarios.schemas import UsuarioInBD

from direcciones.v1.municipios.crud import get_municipios, get_municipio
from direcciones.v1.municipios.schemas import MunicipioOut

municipios = APIRouter(prefix="/v1/municipios", tags=["municipios"])


@municipios.get("", response_model=LimitOffsetPage[MunicipioOut])
async def list_paginate(
    estado_id: int = None,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Listado de municipios"""
    if not current_user.permissions & Permiso.VER_CATALOGOS == Permiso.VER_CATALOGOS:
        raise HTTPException(status_code=403, detail="Forbidden")
    return paginate(get_municipios(db, estado_id))


@municipios.get("/{municipio_id}", response_model=MunicipioOut)
async def detail(
    municipio_id: int,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de una municipio a partir de su id"""
    if not current_user.permissions & Permiso.VER_CATALOGOS == Permiso.VER_CATALOGOS:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        municipio = get_municipio(db, municipio_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MunicipioOut.from_orm(municipio)
