"""
Base de datos

- inicializar
- alimentar
- reiniciar
"""
import os
import click

from sqlalchemy import select, delete

from lib.database import SessionLocal
from direcciones.v1.estados.models import Estado
from direcciones.v1.roles.models import Rol
from direcciones.v1.usuarios.models import Usuario

entorno_implementacion = os.environ.get("DEPLOYMENT_ENVIRONMENT", "develop").upper()


@click.group()
def cli():
    """Base de Datos"""


@click.command()
def inicializar():
    """Inicializar"""
    if entorno_implementacion == "PRODUCTION":
        click.echo("PROHIBIDO: No se inicializa porque este es el servidor de producción.")
        return
    # Borrar estados
    with SessionLocal() as session:
        session.begin()
        session.query(Estado).delete()
        session.query(Usuario).delete()
        session.query(Rol).delete()
        session.commit()
    click.echo("Pendiente inicializar.")


@click.command()
def alimentar():
    """Alimentar"""
    if entorno_implementacion == "PRODUCTION":
        click.echo("PROHIBIDO: No se alimenta porque este es el servidor de producción.")
        return
    click.echo("Pendiente alimentar.")


@click.command()
@click.pass_context
def reiniciar(ctx):
    """Reiniciar ejecuta inicializar y alimentar"""
    ctx.invoke(inicializar)
    ctx.invoke(alimentar)


cli.add_command(inicializar)
cli.add_command(alimentar)
cli.add_command(reiniciar)
