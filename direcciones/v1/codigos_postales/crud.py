"""
Codigos Postales v1, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from direcciones.v1.codigos_postales.models import CodigoPostal
from direcciones.v1.municipios.crud import get_municipio


def get_codigos_postales(
    db: Session,
    municipio_id: int = None,
    cp: int = None,
) -> Any:
    """Consultar los codigos_postales activos"""
    consulta = db.query(CodigoPostal)
    if municipio_id:
        municipio = get_municipio(db, municipio_id)
        consulta = consulta.filter(CodigoPostal.municipio == municipio)
    if cp:
        consulta = consulta.filter_by(cp=cp)
    return consulta.filter_by(estatus="A").order_by(CodigoPostal.cp)


def get_codigo_postal(db: Session, codigo_postal_id: int) -> CodigoPostal:
    """Consultar un codigo_postal por su id"""
    codigo_postal = db.query(CodigoPostal).get(codigo_postal_id)
    if codigo_postal is None:
        raise IndexError("No existe ese código postal")
    if codigo_postal.estatus != "A":
        raise IndexError("No es activo ese código postal, está eliminado")
    return codigo_postal


def get_codigo_postal_cp(db: Session, codigo_postal_cp: int) -> CodigoPostal:
    """Consultar un codigo_postal por su código postal"""
    codigo_postal = db.query(CodigoPostal).filter_by(cp=codigo_postal_cp).first()
    if codigo_postal is None:
        raise IndexError("No existe ese código postal")
    if codigo_postal.estatus != "A":
        raise IndexError("No es activo ese código postal, está eliminado")
    return codigo_postal
