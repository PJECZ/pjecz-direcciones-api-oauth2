"""
Codigos Postales v1, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from direcciones.v1.roles.models import Permiso
from direcciones.v1.usuarios.authentications import get_current_active_user
from direcciones.v1.usuarios.schemas import UsuarioInBD

from direcciones.v1.codigos_postales.crud import get_codigos_postales, get_codigo_postal
from direcciones.v1.codigos_postales.schemas import CodigoPostalOut

codigos_postales = APIRouter(prefix="/v1/codigos_postales", tags=["códigos postales"])


@codigos_postales.get("", response_model=LimitOffsetPage[CodigoPostalOut])
async def list_paginate(
    municipio_id: int = None,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Listado de codigos_postales"""
    if not current_user.permissions & Permiso.VER_CATALOGOS == Permiso.VER_CATALOGOS:
        raise HTTPException(status_code=403, detail="Forbidden")
    return paginate(get_codigos_postales(db, municipio_id))


@codigos_postales.get("/{codigo_postal_id}", response_model=CodigoPostalOut)
async def detail(
    codigo_postal_id: int,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de una codigo_postal a partir de su id"""
    if not current_user.permissions & Permiso.VER_CATALOGOS == Permiso.VER_CATALOGOS:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        codigo_postal = get_codigo_postal(db, codigo_postal_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return CodigoPostalOut.from_orm(codigo_postal)
