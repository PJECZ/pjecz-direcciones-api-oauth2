"""
Base de datos

- inicializar
- alimentar
- reiniciar
"""
import os
import click

from lib.database import Base, engine, SessionLocal

from cli.commands.alimentar_roles import alimentar_roles
from cli.commands.alimentar_usuarios import alimentar_usuarios
from cli.commands.alimentar_estados import alimentar_estados
from cli.commands.alimentar_municipios import alimentar_municipios

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
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    click.echo("Inicializado.")


@click.command()
def alimentar():
    """Alimentar"""
    if entorno_implementacion == "PRODUCTION":
        click.echo("PROHIBIDO: No se alimenta porque este es el servidor de producción.")
        return
    with SessionLocal() as db:
        alimentar_roles(db)
        alimentar_usuarios(db)
        alimentar_estados(db)
        alimentar_municipios(db)
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
