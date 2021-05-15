import click
from actl import Application


@click.command()
@click.argument("application_directory")
def run(application_directory):
    app = Application(application_directory)
    app.run()
