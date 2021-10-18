"""
Alimentar Codigos Postales
"""
from pathlib import Path
import csv

import click
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from direcciones.v1.municipios.models import Municipio
from direcciones.v1.codigos_postales.models import CodigoPostal

CODIGOS_POSTALES_CSV = "seed/codigos-postales-coahuila.csv"


def alimentar_codigos_postales(db: Session):
    """Alimentar codigos postales"""
    ruta = Path(CODIGOS_POSTALES_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando codigos postales...")
    contador = 0
    municipio = None
    codigo_postal = None
    with open(ruta, encoding="iso8859-1") as puntero:
        rows = csv.DictReader(puntero, delimiter="|")
        for row in rows:
            municipio_str = safe_string(row["D_mnpio"])
            if municipio is None or municipio_str != municipio.nombre:
                municipio = db.query(Municipio).filter_by(nombre=municipio_str).first()
            cp_str = safe_string(row["d_codigo"])
            if codigo_postal is None or cp_str != codigo_postal.cp:
                codigo_postal = db.query(CodigoPostal).filter_by(cp=cp_str).first()
                if codigo_postal is None:
                    codigo_postal = CodigoPostal(
                        municipio=municipio,
                        cp=cp_str,
                    )
                    db.add(codigo_postal)
                    contador += 1
        db.commit()
    click.echo(f"  {contador} codigos postales alimentados.")
