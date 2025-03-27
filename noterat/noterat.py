import click

@click.group()
def cli():
    pass

@cli.command()
def add():
    click.echo("[+] Note added!")

@cli.command()
def delete():
    click.echo("[-] Note deleted!")

@cli.command()
def search():
    click.echo("[*] List of notes:")
