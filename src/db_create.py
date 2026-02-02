import sqlite3
from datetime import date

DB_FILE = "database.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Mitglied ( 
	MG_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Vorname TEXT NOT NULL,
    Nachname TEXT NOT NULL,
    Geburtsdatum DATE NOT NULL,
    EMail TEXT NOT NULL,
    Eintrittsdatum DATE NOT NULL
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Sportart ( 
	SPA_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Beitrag FLOAT NOT NULL, 
    Bezeichnung TEXT NOT NULL,
    Ansprechpartner INTEGER NOT NULL 
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS tut ( 
	TUT_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    SPA_ID INTEGER NOT NULL,
    MG_ID INTEGER NOT NULL,
    FOREIGN KEY (SPA_ID) REFERENCES Sportart(SPA_ID),
    FOREIGN KEY (MG_ID) REFERENCES Mitglied(MG_ID)
);
""")





