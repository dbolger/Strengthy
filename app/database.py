import sqlite3
from app import app
from flask import g

# constants
DATABASE_FILE = "../strengthy.db"

# Called when an "appcontext" is closed, usually a request is finished
@app.teardown_appcontext
def close_db_conn(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def database_get():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_FILE)
    return db
