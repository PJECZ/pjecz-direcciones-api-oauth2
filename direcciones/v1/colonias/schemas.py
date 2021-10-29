"""
Colonia v1, esquemas de pydantic
"""
from pydantic import BaseModel


class ColoniaOut(BaseModel):
    """ Esquema para entregar colonia """

    id: int
    estado_id: int
    estado_nombre: str
    municipio_id: int
    municipio_nombre: str
    codigo_postal_id: int
    codigo_postal_cp: int
    nombre: str

    class Config:
        """ SQLAlchemy config """

        orm_mode = True
