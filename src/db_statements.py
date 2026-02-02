import sqlite3

DB_FILE = "database.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def get_cursor():
    con = get_connection()
    return con.cursor()