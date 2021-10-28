"""
Codigos Postales v1, esquemas de pydantic
"""
from pydantic import BaseModel


class CodigoPostalOut(BaseModel):
    """ Esquema para entregar codigo postal """

    id: int
    municipio_id: int
    municipio_nombre: str
    cp: int

    class Config:
        """ SQLAlchemy config """

        orm_mode = True
