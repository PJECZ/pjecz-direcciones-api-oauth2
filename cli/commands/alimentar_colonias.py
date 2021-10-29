"""
Alimentar Colonias
"""
from pathlib import Path
import csv

import click
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from direcciones.v1.codigos_postales.models import CodigoPostal
from direcciones.v1.colonias.models import Colonia

COLONIAS_CSV = "seed/codigos-postales-coahuila.csv"


def alimentar_colonias(db: Session):
    """Alimentar colonias"""
    ruta = Path(COLONIAS_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando colonias...")
    contador = 0
    codigo_postal = None
    colonia = None
    with open(ruta, encoding="iso8859-1") as puntero:
        rows = csv.DictReader(puntero, delimiter="|")
        for row in rows:
            codigo_postal_str = safe_string(row["d_codigo"])
            if codigo_postal is None or int(codigo_postal_str) != codigo_postal.cp:
                codigo_postal = db.query(CodigoPostal).filter_by(cp=int(codigo_postal_str)).first()
            colonia_str = safe_string(row["d_asenta"])
            colonia = Colonia(
                codigo_postal=codigo_postal,
                nombre=colonia_str,
            )
            db.add(colonia)
            contador += 1
            if contador % 100 == 0:
                click.echo(f"  Van {contador} colonias...")
        db.commit()
    click.echo(f"  {contador} colonias alimentados.")
