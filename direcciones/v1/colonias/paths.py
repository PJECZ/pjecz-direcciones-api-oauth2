"""
Colonias v1, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from direcciones.v1.roles.models import Permiso
from direcciones.v1.usuarios.authentications import get_current_active_user
from direcciones.v1.usuarios.schemas import UsuarioInBD

from direcciones.v1.colonias.crud import get_colonias, get_colonia
from direcciones.v1.colonias.schemas import ColoniaOut

colonias = APIRouter(prefix="/v1/colonias", tags=["colonias"])


@colonias.get("", response_model=LimitOffsetPage[ColoniaOut])
async def list_paginate(
    codigo_postal_id: int = None,
    codigo_postal_cp: int = None,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Listado de colonias"""
    if not current_user.permissions & Permiso.VER_CATALOGOS == Permiso.VER_CATALOGOS:
        raise HTTPException(status_code=403, detail="Forbidden")
    return paginate(get_colonias(db, codigo_postal_id, codigo_postal_cp))


@colonias.get("/{colonia_id}", response_model=ColoniaOut)
async def detail(
    colonia_id: int,
    current_user: UsuarioInBD = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Detalle de una colonia a partir de su id"""
    if not current_user.permissions & Permiso.VER_CATALOGOS == Permiso.VER_CATALOGOS:
        raise HTTPException(status_code=403, detail="Forbidden")
    try:
        colonia = get_colonia(db, colonia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return ColoniaOut.from_orm(colonia)
