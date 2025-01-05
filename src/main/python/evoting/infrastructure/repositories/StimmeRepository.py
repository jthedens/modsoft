import sqlite3

def stimmeSumme(abstimmungid, stimme):
    try:
        # Verbindung zur Datenbank mit 'with' für automatische Schließung
        with sqlite3.connect("eVoteMain.db") as conn:
            # Cursor-Objekt erstellen
            cursor = conn.cursor()

            # SQL-Abfrage, um die Anzahl der Stimmen zu zählen
            cursor.execute("SELECT COUNT(stimme) FROM auswertung WHERE abstimmungid = ? AND stimme = ?", (abstimmungid, stimme))

            # Ergebnis abrufen
            count = cursor.fetchone()

            # Überprüfen, ob ein Ergebnis vorhanden ist
            if count is not None:
                return count[0]  # Der erste Wert der Abfrage (Anzahl der Stimmen)
            else:
                return 0  # Falls keine Daten vorhanden sind, 0 zurückgeben

    except sqlite3.Error as e:
        # Fehlerbehandlung
        print(f"Fehler bei der Datenbankabfrage: {e}")
        return None
