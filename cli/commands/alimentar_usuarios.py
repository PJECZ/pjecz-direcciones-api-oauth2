"""
Alimentar Usuarios
"""
from pathlib import Path
import csv

import click
from sqlalchemy.orm import Session
from lib.pwgen import generar_contrasena

from direcciones.v1.roles.models import Rol
from direcciones.v1.usuarios.models import Usuario

USUARIOS_CSV = "seed/usuarios.csv"


def alimentar_usuarios(db: Session):
    """Alimentar usuarios"""
    ruta = Path(USUARIOS_CSV)
    if not ruta.exists():
        click.echo(f"AVISO: {ruta.name} no se encontró.")
        return
    if not ruta.is_file():
        click.echo(f"AVISO: {ruta.name} no es un archivo.")
        return
    click.echo("Alimentando usuarios...")
    contador = 0
    with open(ruta, encoding="utf8") as puntero:
        rows = csv.DictReader(puntero)
        for row in rows:
            rol = db.query(Rol).get(int(row["rol_id"]))
            db.add(
                Usuario(
                    rol=rol,
                    email=row["email"],
                    nombres=row["nombres"],
                    apellido_paterno=row["apellido_paterno"],
                    apellido_materno=row["apellido_materno"],
                    estatus=row["estatus"],
                    contrasena=generar_contrasena(),
                )
            )
            contador += 1
        db.commit()
    click.echo(f"  {contador} usuarios alimentados.")
