import sqlite3

def stimmeErfassen(buergerid, abstimmungid, stimme):
    try:
        # Verbindung zur Datenbank herstellen mit 'with' für automatische Schließung
        with sqlite3.connect("eVoteMain.db") as connection:
            cursor = connection.cursor()

            # SQL-Befehl zum Einfügen eines Eintrags
            insert_query = '''INSERT INTO auswertung (buergerid, abstimmungid, stimme) VALUES (?, ?, ?)'''

            # Werte, die eingefügt werden sollen
            values = (buergerid, abstimmungid, stimme)

            # SQL-Befehl ausführen
            cursor.execute(insert_query, values)

            # Änderungen speichern
            connection.commit()

            print("Eintrag erfolgreich hinzugefügt.")

    except sqlite3.Error as e:
        # Fehlerbehandlung, falls ein Fehler bei der Datenbankoperation auftritt
        print(f"Fehler beim Hinzufügen des Eintrags: {e}")
