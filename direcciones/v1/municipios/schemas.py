"""
Municipios v1, esquemas de pydantic
"""
from pydantic import BaseModel


class MunicipioOut(BaseModel):
    """ Esquema para entregar municipio """

    id: int
    estado_id: int
    estado_nombre: str
    nombre: str

    class Config:
        """ SQLAlchemy config """

        orm_mode = True
