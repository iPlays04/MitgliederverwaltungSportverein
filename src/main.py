import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()
DB_FILE = "database.db"

class MitgliedCreate(BaseModel):
    Vorname: str
    Nachname: str
    Geburtsdatum: date
    Email: str
    Eintrittsdatum: date

class SportartCreate(BaseModel):
    Beitrag:float
    Bezeichnung:str
    Ansprechpartner:int

@app.get("/mitglieder")
def get_mitglieder():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM Mitglied")
    rows = cur.fetchall()

    con.close()

    return [dict(row) for row in rows]

@app.get("/sportarten")
def get_sportarten():
    con = sqlite3.connect(DB_FILE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM Sportart")
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

@app.post("/sportarten")
def create_mitglied(m: SportartCreate):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    cur.execute("""
        INSERT INTO Sportart 
        (Beitrag, Bezeichnung, Ansprechpartner)
        VALUES (?, ?, ?)
    """, (
        m.Beitrag,
        m.Bezeichnung,
        m.Ansprechpartner
    ))

    con.commit()
    mitglied_id = cur.lastrowid
    con.close()

    return {
        "status": "Mitglied erfolgreich angelegt",
        "MG_ID": mitglied_id
    }

from fastapi import HTTPException

@app.delete("/mitglieder/{mitglied_id}")
def delete_mitglied(mitglied_id: int):
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()

    # Prüfen, ob das Mitglied existiert
    cur.execute("SELECT * FROM Mitglied WHERE MG_ID = ?", (mitglied_id,))
    if cur.fetchone() is None:
        con.close()
        raise HTTPException(status_code=404, detail="Mitglied nicht gefunden")

    # Mitglied löschen
    cur.execute("DELETE FROM Mitglied WHERE MG_ID = ?", (mitglied_id,))
    con.commit()
    con.close()

    return {"status": "Mitglied erfolgreich gelöscht", "MG_ID": mitglied_id}
