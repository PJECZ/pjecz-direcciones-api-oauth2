"""
Alimentar Roles
"""
from pathlib import Path
import csv

import click
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from direcciones.v1.roles.models import Rol

ROLES_CSV = "seed/roles.csv"


def alimentar_roles(db: Session):
    """Alimentar roles"""
    ruta = Path(ROLES_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando roles...")
    contador = 0
    with open(ruta, encoding="utf8") as puntero:
        rows = csv.DictReader(puntero)
        for row in rows:
            db.add(
                Rol(
                    nombre=safe_string(row["nombre"]),
                    permiso=int(row["permiso"]),
                    estatus=row["estatus"],
                )
            )
            contador += 1
        db.commit()
    click.echo(f"  {contador} roles alimentados.")
