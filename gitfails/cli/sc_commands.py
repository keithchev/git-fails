import os
import pathlib
import shutil
import click

from gitfails import logger, utils
from gitfails.config import read_config
from gitfails.scenarios import scenario_classes


@click.command()
def list_scenarios():
    click.echo('Available scenarios:')
    for name in scenario_classes.keys():
        click.echo('- %s' % utils.camel_case_to_snake_case(name).replace('_', '-'))


@click.command()
@click.argument('name')
@click.option('overwrite', '-o', '--overwrite', is_flag=True, default=False)
def create_scenario(name, overwrite):

    class_name = utils.snake_case_to_camel_case(name.replace('-', '_'))
    if class_name not in scenario_classes.keys():
        click.echo("Invalid scenario name: '%s'" % name)
        return

    def dirpath(ind):
        return pathlib.Path(read_config()['working_dir']) / f'{name}-{ind}'

    ind = 1
    if not overwrite:
        while os.path.exists(dirpath(ind)):
            ind += 1

    ScenarioClass = scenario_classes[class_name]
    scenario = ScenarioClass(dirpath(ind), overwrite=overwrite)
    scenario.construct()
    click.echo('Created scenario %s at %s' % (name, dirpath(ind)))


@click.command()
def delete_scenarios():
    """
    Cleanup by removing all scenarios
    WARNING: this deletes all repos/files in the root directory.
    """
    config = read_config()
    for subdirpath in pathlib.Path(config['working_dir']).iterdir():
        if subdirpath.is_dir():
            shutil.rmtree(subdirpath)

    click.echo('Removed all scenarios from %s' % config['working_dir'])
