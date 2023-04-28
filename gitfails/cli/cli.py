import click

from gitfails import logger
from gitfails.cli.config_commands import reset_config, set_working_dir, view_config
from gitfails.cli.sc_commands import create_scenario, delete_scenarios, list_scenarios
from gitfails.config import init_config, read_config

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@click.group()
@click.pass_context
def scenario_commands(ctx):
    """Scenario commands"""
    pass


@click.group()
@click.pass_context
def config_commands(ctx):
    """config commands"""
    pass


@click.command()
def init():
    '''
    Top-level initialization and setup
    '''
    init_config()
    click.echo('Initialized config file')


config_commands.add_command(view_config, 'view')
config_commands.add_command(view_config, 'show')
config_commands.add_command(reset_config, 'reset')
config_commands.add_command(set_working_dir)

scenario_commands.add_command(list_scenarios, 'ls')
scenario_commands.add_command(create_scenario, 'create')
scenario_commands.add_command(delete_scenarios, 'remove')

cli.add_command(config_commands, 'config')
cli.add_command(scenario_commands, 'sc')

cli.add_command(init)
