import os
import pathlib
import shutil
import click

from gitfails import logger
from gitfails.config import read_config
from gitfails.scenarios import ALL_SCENARIOS


@click.command()
def list_scenarios():
    for name in ALL_SCENARIOS.keys():
        print(name)


@click.command()
@click.argument('name')
def create_scenario(name):

    name = name.replace('-', '_')
    if name not in ALL_SCENARIOS.keys():
        logger.error('Invalid scenario name: %s' % name)
        return

    dirpath = lambda ind: pathlib.Path(read_config()['working_dir']) / f'{name}-{ind}'
    ind = 1
    while os.path.exists(dirpath(ind)):
        ind += 1

    scenario = ALL_SCENARIOS[name](dirpath(ind))
    scenario.construct()
    logger.info('Created scenario %s' % name)


@click.command()
def delete_scenarios():
    """
    Cleanup by removing all scenarios
    WARNING: this deletes all repos/files in the root directory.
    """
    config = read_config()
    logger.info('Removing all scenarios from %s' % config['working_dir'])
    for subdirpath in pathlib.Path(config['working_dir']).iterdir():
        if subdirpath.is_dir():
            shutil.rmtree(subdirpath)
