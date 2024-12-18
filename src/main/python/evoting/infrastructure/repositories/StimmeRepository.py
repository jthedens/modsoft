import sqlite3

def countStimme(abstimmungs_id, citizens_id):
    # Zugriff auf die Datenbank
    conn = sqlite3.connect("../../../../stimmen.db")

    # Cursor-Objekt erstellen
    cursor = conn.cursor()

    # SQL-Abfrage, um die Anzahl der Werte in der Spalte 'name' zu zählen
    cursor.execute("SELECT COUNT(STIMME) FROM stimmen WHERE ABSTIMMUNGSID = ? AND CITIZENSID = ?",(abstimmungs_id, citizens_id))

    # Ergebnis abrufen
    count = cursor.fetchone()[0]

    conn.close()

    return count

