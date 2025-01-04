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


def abstimmungenListen(buerger_alter):
    """
    Listet die Abstimmungen, bei denen der Bürger teilnehmen darf, und die aktiv sind.

    :param buerger_alter: Alter des Bürgers
    :return: Liste der zulässigen Abstimmungen
    """
    import sqlite3

    try:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect("eVoteMain.db")
        cursor = conn.cursor()

        # SQL-Abfrage für aktive Abstimmungen
        cursor.execute("""
            SELECT 
                abstimmungid, 
                titel, 
                beschreibung, 
                frist, 
                altersgrenze, 
                status 
            FROM abstimmung
            WHERE status = 1
        """)

        # Alle Ergebnisse abrufen
        abstimmungen = cursor.fetchall()

        # Filter für Alter anwenden
        erlaubte_abstimmungen = [
            abstimmung for abstimmung in abstimmungen
            if buerger_alter >= abstimmung[4]  # Altersgrenze prüfen
        ]

        return erlaubte_abstimmungen

    except sqlite3.Error as e:
        # Fehler in der Datenbankbehandlung
        raise Exception(f"Datenbankfehler: {e}")

    finally:
        # Verbindung schließen
        if conn:
            conn.close()


