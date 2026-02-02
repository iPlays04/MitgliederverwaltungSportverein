import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()
DB_FILE = "..\database.db"

class MitgliedCreate(BaseModel):
    Vorname: str
    Nachname: str
    Geburtsdatum: date
    Email: str
    Eintrittsdatum: date

@app.get("/mitglieder")
def get_mitglieder():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM Mitglied")
    rows = cur.fetchall()

    con.close()

    return [dict(row) for row in rows]

@app.post("/mitglieder")
def create_mitglied(m: MitgliedCreate):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Mitglied 
        (Vorname, Nachname, Geburtsdatum, Email, Eintrittsdatum)
        VALUES (?, ?, ?, ?, ?)
    """, (
        m.Vorname,
        m.Nachname,
        m.Geburtsdatum,
        m.Email,
        m.Eintrittsdatum
    ))

    con.commit()
    mitglied_id = cur.lastrowid
    con.close()

    return {
        "status": "Mitglied erfolgreich angelegt",
        "MG_ID": mitglied_id
    }

