"""
Estados v1, esquemas de pydantic
"""
from pydantic import BaseModel


class EstadoOut(BaseModel):
    """Esquema para entregar estado"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
