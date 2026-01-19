import sqlite3

DB_FILE = "database.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()