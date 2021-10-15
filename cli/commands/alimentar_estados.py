"""
Alimentar Estados
"""
from pathlib import Path
import csv

import click
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from direcciones.v1.estados.models import Estado

ESTADOS_CSV = "seed/estados.csv"


def alimentar_estados(db: Session):
    """Alimentar estados"""
    ruta = Path(ESTADOS_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando estados...")
    contador = 0
    with open(ruta, encoding="utf8") as puntero:
        rows = csv.DictReader(puntero)
        for row in rows:
            db.add(
                Estado(
                    nombre=safe_string(row["nombre"]),
                    estatus=row["estatus"],
                )
            )
            contador += 1
        db.commit()
    click.echo(f"  {contador} estados alimentados.")
