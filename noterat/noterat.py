import click
import sqlite3

from rich import box
from rich.console import Console
from rich.table import Table


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx):
    """Noterat.

    This is a simple note taking CLI.
    """
    con = sqlite3.Connection("notes.db")
    ctx.obj = con
    cur = con.cursor()
    sql = r"""
    CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY, 
            note TEXT, 
            date DATETIME DEFAULT CURRENT_TIMESTAMP
            )"""
    cur.execute(sql)
    con.commit()


@cli.command("add", short_help="Add a note.")
@click.argument("note")
@click.pass_obj
def add_note(con, note: str) -> None:
    con.cursor().execute(f"INSERT INTO notes (note) VALUES ('{note}');")
    con.commit()
    click.echo(f"[+] Note added: {note}")


@cli.command("get", short_help="Get a note.")
@click.argument("note_id")
def get_note(note_id: str) -> None:
    res = cur.execute(
        f"SELECT note FROM notes WHERE id = {note_id};"
    ).fetchone()
    click.echo(f"{res}")


@cli.command("list", short_help="List all notes.")
@click.pass_obj
def list_notes(con) -> None:
    console = Console()
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("Note", style="yellow", justify="left")
    table.add_column("Date", style="red", justify="left")
    res = (
        con.cursor()
        .execute("SELECT note, date FROM notes ORDER BY date DESC;")
        .fetchall()
    )
    for note in res:
        table.add_row(
            note[0],
            str(note[1]),
        )
    console.print(table)


@cli.command("delete", short_help="Delete a note.")
def delete():
    click.echo("[-] Note deleted!")


@cli.command("find", short_help="Find a note by text.")
def find():
    click.echo("[*] List of notes:")


@cli.command("backup", short_help="Backup db.")
def backup():
    click.echo("[*] List of notes:")
