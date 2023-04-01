import click
from gitfails import logger


@click.command()
def sc_list():
    """List pre-defined scenarios"""
    logger.info('Listing scenarios')


@click.command()
@click.argument('name')
def sc_create(name):
    """Construct a scenario"""
    logger.info(f'Constructing scenario {name}')
