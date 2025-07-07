import sqlite3


class Db:
    def __init__(self, db_path: str = None):
        self.db_path = db_path

    def __enter__(self) -> sqlite3.Cursor:
        self.db_con = sqlite3.connect(self.db_path)
        self.db_con.execute("PRAGMA foreign_keys = 1")
        return self.db_con.cursor()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.db_con.commit()
        self.db_con.close()

    def initialize(self) -> None:
        db_config = r"""
            PRAGMA journal_mode = WAL;
            PRAGMA synchronous = NORMAL;
            """

        notes_tbl = r"""
            CREATE TABLE IF NOT EXISTS notes (
                note_id INTEGER PRIMARY KEY, 
                note TEXT NOT NULL, 
                date DATETIME DEFAULT CURRENT_TIMESTAMP
                );"""

        tags_tbl = r"""
            CREATE TABLE IF NOT EXISTS tags (
                tag_id INTEGER PRIMARY KEY,
                tag TEXT
                );"""

        notes_tags_tbl = """
            CREATE TABLE IF NOT EXISTS tags_notes (
            note_id INTEGER PRIMARY KEY,
            tag_id INTEGER NOT NULL 
            );"""

        init_db_script = f"{db_config + notes_tbl + tags_tbl + notes_tags_tbl}"
        con = sqlite3.connect(self.db_path)
        con.executescript(init_db_script)
        con.close()
