"""
Municipios v1, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Municipio(Base, UniversalMixin):
    """ Municipio """

    # Nombre de la tabla
    __tablename__ = 'municipios'

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    estado_id = Column(Integer, ForeignKey('estados.id'), index=True, nullable=False)
    estado = relationship('Estado', back_populates='municipios')

    # Columnas
    nombre = Column(String(256), nullable=False)

    # Hijos
    codigos_postales = relationship('CodigoPostal', back_populates='municipio')

    def __repr__(self):
        """ Representación """
        return f"<Municipio {self.nombre}>"
