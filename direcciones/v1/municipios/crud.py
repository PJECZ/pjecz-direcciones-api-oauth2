"""
Municipios v1, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from direcciones.v1.estados.crud import get_estado
from direcciones.v1.municipios.models import Municipio


def get_municipios(
    db: Session,
    estado_id: int = None,
) -> Any:
    """ Consultar los municipios activos """
    consulta = db.query(Municipio)
    if estado_id:
        estado = get_estado(db, estado_id)
        consulta = consulta.filter(Municipio.estado == estado)
    return consulta.filter_by(estatus="A").order_by(Municipio.nombre)


def get_municipio(db: Session, municipio_id: int) -> Municipio:
    """ Consultar un municipio por su id """
    municipio = db.query(Municipio).get(municipio_id)
    if municipio is None:
        raise IndexError("No existe ese municipio")
    if municipio.estatus != "A":
        raise IndexError("No es activo ese municipio, está eliminado")
    return municipio
