import click
import sqlite3


from rich import box
from rich.console import Console
from rich.table import Table
from pathlib import Path

from .db import Db


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx):
    """Noterat.

    This is a simple note taking CLI.
    """
    # db_path = Path.home() / ".local" / "share" / "noterat.db"
    db_path = Path("noterat.db")
    db = Db(db_path)
    if not db_path.exists():
        db.initialize()
    ctx.obj = db


@cli.command("add", short_help="Add a note.")
@click.argument("note")
@click.pass_obj
def add_note(db, note: str) -> None:
    with db as cur:
        cur.execute("INSERT INTO notes (note) VALUES (?);", (note,))
    click.echo(click.style(f"[+] Note added: {note}", fg="green"))


@cli.command("list", short_help="List all notes.")
@click.option(
    "-s",
    "--sort",
    default="date",
    show_default=True,
    type=click.Choice(["date", "id"], case_sensitive=False),
)
@click.option(
    "-o",
    "--order",
    default="desc",
    show_default=True,
    type=click.Choice(["desc", "asc"], case_sensitive=False),
)
@click.pass_obj
def list_notes(db: click.Context, sort: str, order: str) -> None:
    console = Console()
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("Id", style="magenta", justify="left")
    table.add_column("Note", style="green", justify="left")
    table.add_column("Date", style="yellow", justify="left")
    if sort == "id":
        sort = f"note_{sort}"
    with db as cur:
        res = cur.execute(
            f"SELECT note_id, note, date FROM notes ORDER BY {sort} {order};",
        ).fetchall()
    for note in res:
        table.add_row(
            str(note[0]),
            note[1],
            str(note[2]),
        )
    console.print(table)


@cli.command("delete", short_help="Delete a note.")
def delete():
    raise NotImplementedError


@cli.command("find", short_help="Find a note by string.")
@click.argument("str_to_find")
@click.pass_obj
def find(db: click.Context, str_to_find: str) -> None:
    console = Console()
    table = Table(box=box.SIMPLE, show_header=False)
    table.add_column("Note", style="green", justify="left")
    table.add_column("Date", style="yellow", justify="left")

    with db as cur:
        res = cur.execute(
            f"SELECT note, date FROM notes WHERE note LIKE '%{str_to_find}%';"
        ).fetchall()

    if not res:
        click.echo(
            click.style(
                f"[*] No notes found using: '{str_to_find}'", fg="yellow"
            )
        )
        return

    for note in res:
        table.add_row(
            note[0],
            str(note[1]),
        )
    console.print(table)


@cli.command("reinit", short_help="Reinitialize the database.")
def reinitialize():
    raise NotImplementedError


@cli.command("backup", short_help="Backup all notes.")
def backup():
    raise NotImplementedError
