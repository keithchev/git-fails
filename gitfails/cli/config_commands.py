import os
import pathlib
import click

from gitfails import logger
from gitfails.config import init_config, read_config, write_config


@click.command()
def view_config():
    config = read_config()
    click.echo(config)


@click.command()
def reset_config():
    init_config(reset=True)


@click.command()
@click.argument('path')
def set_working_dir(path):
    """Set the top-level directory (in which repos are created)"""

    config = read_config()
    config['working_dir'] = str(pathlib.Path(path).expanduser().resolve())

    os.makedirs(config['working_dir'], exist_ok=True)
    write_config(config)

    click.echo('Set working directory to %s' % config['working_dir'])
