"""
Estados v1, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from direcciones.v1.estados.models import Estado
from direcciones.v1.estados.schemas import EstadoOut


def get_estados(db: Session) -> Any:
    """Consultar los estados activos"""
    return db.query(Estado).filter_by(estatus="A").order_by(Estado.nombre)


def get_estado(db: Session, estado_id: int) -> EstadoOut:
    """Consultar un estado por su id"""
    estado = db.query(Estado).get(estado_id)
    if estado is None:
        raise IndexError("No existe ese estado")
    if estado.estatus != "A":
        raise IndexError("No es activo ese estado, está eliminado")
    return estado
