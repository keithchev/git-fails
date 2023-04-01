import click

from gitfails import logger
from gitfails.cli.sc_commands import sc_create, sc_list

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@click.group()
@click.pass_context
def sc(ctx):
    """Scenario commands"""
    pass


@click.command()
@click.argument('path')
def set_working_dir(path):
    """Set the top-level working directory (in which repos are created)"""
    logger.info('Setting working directory to %s' % path)


@click.command()
def cleanup():
    """
    Cleanup by removing all scenarios

    WARNING: this deletes all repos/files in the working directory.
    """
    logger.info('Deleting all repos from working directory')


cli.add_command(set_working_dir)
cli.add_command(cleanup)

sc.add_command(sc_list, 'list')
sc.add_command(sc_create, 'create')
cli.add_command(sc)


if __name__ == '__main__':
    cli()
