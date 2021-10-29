"""
Colonias v1, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from direcciones.v1.colonias.models import Colonia
from direcciones.v1.codigos_postales.crud import get_codigo_postal


def get_colonias(
    db: Session,
    codigo_postal_id: int = None,
) -> Any:
    """ Consultar los colonias activos """
    consulta = db.query(Colonia)
    if codigo_postal_id:
        codigo_postal = get_codigo_postal(db, codigo_postal_id)
        consulta = consulta.filter(Colonia.codigo_postal == codigo_postal)
    return consulta.filter_by(estatus="A").order_by(Colonia.nombre)


def get_colonia(db: Session, colonia_id: int) -> Colonia:
    """ Consultar un colonia por su id """
    colonia = db.query(Colonia).get(colonia_id)
    if colonia is None:
        raise IndexError("No existe ese ___")
    if colonia.estatus != "A":
        raise IndexError("No es activa ese ___, está eliminado")
    return colonia
