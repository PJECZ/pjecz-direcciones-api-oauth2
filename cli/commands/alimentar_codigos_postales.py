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
    with open(ruta, encoding="iso8859-1") as puntero:
        rows = csv.DictReader(puntero, delimiter="|")
        acumulados = []
        for row in rows:
            cp = safe_string(row["d_codigo"])
            municipio = db.query(Municipio).filter_by(nombre=safe_string(row["D_mnpio"])).first()
            if cp not in acumulados:
                db.add(
                    CodigoPostal(
                        municipio=municipio,
                        cp=cp,
                    )
                )
                acumulados.append(cp)
                contador += 1
        db.commit()
    click.echo(f"  {contador} codigos postales alimentados.")
