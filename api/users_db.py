import sqlite3
from flask import g
from api.config import users_db

def get_db() -> sqlite3.Connection:
    if 'db' not in g:
        g.db = sqlite3.connect(users_db) #sqlite3.connect() method. This method establishes a connection to the specified database file. If the file does not exist, SQLite will automatically create it. 
    return g.db