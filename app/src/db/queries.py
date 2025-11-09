from .connection import db

def execute(sql, params=None):
    cur = db.cursor()
    cur.execute(sql, params or ())
    return cur

def fetch(sql, params=None):
    cur = execute(sql, params)
    return cur.fetchone()

def fetch_all(sql, params=None):
    cur = execute(sql, params)
    return cur.fetchall()
    