import sqlite3


class Db:
    def __init__(self, db_config: str = None):
        self._connection = sqlite3.connect(db_config)

    def initalize(self):
        notes_tbl = r"""
            CREATE TABLE IF NOT EXISTS notes (
                note_id INTEGER PRIMARY KEY, 
                note TEXT NOT NULL, 
                date DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""

        tags_tbl = r"""
            CREATE TABLE IF NOT EXISTS tags (
                tag_id INTEGER PRIMARY KEY,
                tag TEXT
                )"""

        tags_notes_tbl = """
            CREATE TABLE IF NOT EXISTS tags_notes (
            tag_id INTEGER NOT NULL, 
            note_id INTEGER NOT NULL
            )"""

    def close(self):
        self._connection.close()
