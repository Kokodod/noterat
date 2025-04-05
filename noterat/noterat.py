import click
import sqlite3

class noterat:
    def __init__(self, connection)

@click.group()
@click.version_option()
def cli():
    """Noterat.

    This is a simple note taking CLI.
    """

@click.group()
def note():
    """Manages notes."""

@cli.command("add", short_help="Add a note.")
@click.argument("note")
@click.argument("tag", required=False)
def add(note: str, tag: str):
    if len(note) > 15:
        note = f"{note[0:14]}..."
    click.echo(f"[+] Note: {note} - Tag: {tag}")


@cli.command()
def delete():
    click.echo("[-] Note deleted!")


@cli.command()
def search():
    click.echo("[*] List of notes:")
