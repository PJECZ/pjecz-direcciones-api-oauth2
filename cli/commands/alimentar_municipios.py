"""
Alimentar Municipios
"""
from pathlib import Path
import csv

import click
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from direcciones.v1.estados.models import Estado
from direcciones.v1.municipios.models import Municipio

MUNICIPIOS_CSV = "seed/codigos-postales-coahuila.csv"


def alimentar_municipios(db: Session):
    """Alimentar municipios"""
    ruta = Path(MUNICIPIOS_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    estado = db.query(Estado).filter_by(nombre="COAHUILA DE ZARAGOZA").first()
    if estado is None:
        click.echo(f"AVISO: No existe {estado.nombre} en la base de datos.")
        return
    click.echo("Alimentando municipios...")
    contador = 0
    estado = None
    municipio = None
    with open(ruta, encoding="iso8859-1") as puntero:
        rows = csv.DictReader(puntero, delimiter="|")
        for row in rows:
            estado_str = safe_string(row["d_estado"])
            if estado is None or estado_str != estado.nombre:
                estado = db.query(Estado).filter_by(nombre=estado_str).first()
            municipio_str = safe_string(row["D_mnpio"])
            if municipio is None or municipio_str != municipio.nombre:
                municipio = db.query(Municipio).filter_by(nombre=municipio_str).first()
                if municipio is None:
                    municipio = Municipio(
                        estado=estado,
                        nombre=municipio_str,
                    )
                    db.add(municipio)
                    contador += 1
        db.commit()
    click.echo(f"  {contador} municipios alimentados.")
