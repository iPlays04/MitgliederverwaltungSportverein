import sqlite3

DB_FILE = "database.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS Mitglied ( 
	MG_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Vorname TEXT NOT NULL,
    Nachname TEXT NOT NULL,
    Geburtsdatum INTEGER NOT NULL,
    E-Mail TEXT NOT NULL,
    Eintrittsdatum INTEGER NOT NULL, 
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Sportart ( 
	SPA_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Beitrag FLOAT NOT NULL, 
    Bezeichnung TEXT NOT NULL,
    Ansprechpartner INTEGER NOT NULL, 
);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS tut ( 
	TUT_ID TEXT NOT NULL PRIMARY KEY AUTOINCREMENT,
    FOREIGN KEY (SPA_ID) REFERENCES Sportart(SPA_ID),
    FOREIGN KEY (MG_ID) REFERENCES Mitglieder(MG_ID)
);
""")

