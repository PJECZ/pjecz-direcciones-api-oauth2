"""
Codigos Postales v1, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class CodigoPostal(Base, UniversalMixin):
    """CodigoPostal"""

    # Nombre de la tabla
    __tablename__ = "codigos_postales"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    municipio_id = Column(Integer, ForeignKey("municipios.id"), index=True, nullable=False)
    municipio = relationship("Municipio", back_populates="codigos_postales")

    # Columnas
    cp = Column(Integer, unique=True, nullable=False)

    # Hijos
    colonias = relationship("Colonia", back_populates="codigo_postal")

    @property
    def municipio_nombre(self):
        """Nombre del municipio"""
        return self.municipio.nombre

    def __repr__(self):
        """Representación"""
        return f"<CodigoPostal {self.cp}>"
