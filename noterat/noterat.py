import click

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo("[*] Initialize database!")

@cli.command()
def dropdb():
    click.echo("[*] Dropped the database!")
