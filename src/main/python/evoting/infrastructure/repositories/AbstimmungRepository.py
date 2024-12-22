import sqlite3
import logging

def abstimmungFinden(abstimmungid):
    """
    Sucht eine Abstimmung in der Datenbank basierend auf der Abstimmungs-ID.
    Gibt ein Dictionary mit Abstimmungsdetails zurück, falls gefunden.
    """
    try:
        # Verbindung zur Datenbank herstellen
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            # SQL-Abfrage ausführen
            cursor.execute(
                """
                SELECT 
                    abstimmungid, 
                    titel,
                    beschreibung, 
                    frist, 
                    altersgrenze, 
                    status
                FROM abstimmung 
                WHERE abstimmungid = ?
                """,
                (abstimmungid,)
            )

            # Ergebnis abrufen
            result = cursor.fetchone()

            if result is None:
                raise ValueError(f"Abstimmung mit ID {abstimmungid} wurde nicht gefunden.")

            # Ergebnisse entpacken
            abstimmungid, titel, beschreibung, frist, altersgrenze, status = result

            # Abstimmungsinformationen zurückgeben
            return {
                "abstimmungid": abstimmungid,
                "titel": titel,
                "beschreibung": beschreibung,
                "frist": frist,
                "altersgrenze": altersgrenze,
                "status": status
            }

    except sqlite3.Error as e:
        # Datenbankfehler protokollieren
        logging.error(f"Datenbankfehler bei Abstimmungssuche: {e}")
        raise
    except ValueError as e:
        # Falls keine Daten gefunden wurden
        logging.warning(f"Fehler: {e}")
        raise
