"""
Colonias v1, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Colonia(Base, UniversalMixin):
    """Colonia"""

    # Nombre de la tabla
    __tablename__ = "colonias"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    codigo_postal_id = Column(Integer, ForeignKey("codigos_postales.id"), index=True, nullable=False)
    codigo_postal = relationship("CodigoPostal", back_populates="colonias")

    # Columnas
    nombre = Column(String(256), nullable=False)

    @property
    def codigo_postal_cp(self):
        """Codigo Postal"""
        return self.codigo_postal.cp

    @property
    def municipio_id(self):
        """ID del municipio"""
        return self.codigo_postal.municipio_id

    @property
    def municipio_nombre(self):
        """Nombre del municipio"""
        return self.codigo_postal.municipio.nombre

    @property
    def estado_id(self):
        """ID del estado"""
        return self.codigo_postal.municipio.estado_id

    @property
    def estado_nombre(self):
        """Nombre del estado"""
        return self.codigo_postal.municipio.estado.nombre

    def __repr__(self):
        """Representación"""
        return f"<Colonia {self.nombre}>"
