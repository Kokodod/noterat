import sqlite3


class Db:
    IN_MEMORY = ":memory:"
    DB_PATH = ""

    def __init__(self, db_path: str = None):
        if db_path:
            self._connection = sqlite3.connect(db_path)
        else:
            self._connection = sqlite3.connect(Db.IN_MEMORY)

    def close(self):
        self._connection.close()
