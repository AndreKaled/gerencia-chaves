import psycopg
import os

class Database:
    def __init__(self):
        self.conn = None
    
    def connect(self):
        if self.conn is None:
            self.conn = psycopg.connect(
                host=os.getenv("DB_HOST", "localhost"),
                dbname=os.getenv("DB_NAME", "chaves"),
                user=os.getenv("DB_USER", "admin"),
                password=os.getenv("DB_PASS", "admin"),
            )
            self.conn.autocommit = True

    def cursor(self):
        if self.conn is None:
            self.connect()
        return self.conn.cursor(row_factory=psycopg.rows.dict_row)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

db = Database()