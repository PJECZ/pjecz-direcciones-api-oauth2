"""
Comandos Click para instalar con pip install --editable .
"""
from setuptools import setup


setup(
    name="direcciones",
    version="0.1",
    packages=["direcciones"],
    entry_points="""
        [console_scripts]
        direcciones=cli.cli:cli
    """,
)
