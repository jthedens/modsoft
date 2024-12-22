import sqlite3
import logging
import os


# Allgemeine Einstellungen für Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def datenbank_verbindung_pruefen():
    """Überprüft, ob die Datenbankdatei existiert."""
    if not os.path.exists("eVoteMain.db"):
        raise ValueError("Die Datenbankdatei existiert nicht!")


def abstimmungErstellen(abstimmungid, titel, beschreibung, frist, altersgrenze, status):
    """
    Erstellt eine neue Abstimmung in der Datenbank.
    """
    try:
        datenbank_verbindung_pruefen()

        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()

            # Überprüfen, ob die Abstimmungs-ID bereits existiert
            cursor.execute("SELECT COUNT(*) FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            if cursor.fetchone()[0] > 0:
                raise ValueError("Die AbstimmungsID existiert bereits!")

            # Abstimmung einfügen
            cursor.execute("""
            INSERT INTO abstimmung (
                abstimmungid, titel, beschreibung, frist, altersgrenze, status
            ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                abstimmungid,
                titel,
                beschreibung,
                frist,
                altersgrenze,
                status
            ))

            conn.commit()
            logging.info(f"Abstimmung mit ID {abstimmungid} erfolgreich erstellt!")
    except sqlite3.Error as e:
        logging.error(f"Datenbankfehler beim Hinzufügen der Abstimmung: {e}")
        raise
    except ValueError as ve:
        logging.warning(f"Fehler bei der Eingabe: {ve}")
        raise


def abstimmungFinden(abstimmungid):
    """
    Sucht eine Abstimmung in der Datenbank basierend auf der Abstimmungs-ID.
    Gibt ein Dictionary mit Abstimmungsdetails zurück, falls gefunden.
    """
    try:
        datenbank_verbindung_pruefen()

        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    abstimmungid, 
                    titel,
                    beschreibung, 
                    frist, 
                    altersgrenze, 
                    status
                FROM abstimmung 
                WHERE abstimmungid = ?
                """, (abstimmungid,))

            result = cursor.fetchone()

            if result is None:
                raise ValueError(f"Abstimmung mit ID {abstimmungid} wurde nicht gefunden.")

            abstimmungid, titel, beschreibung, frist, altersgrenze, status = result
            return {
                "abstimmungid": abstimmungid,
                "titel": titel,
                "beschreibung": beschreibung,
                "frist": frist,
                "altersgrenze": altersgrenze,
                "status": status
            }

    except sqlite3.Error as e:
        logging.error(f"Datenbankfehler bei der Abstimmungssuche: {e}")
        raise
    except ValueError as e:
        logging.warning(f"Warnung: {e}")
        raise


def abstimmungUpdate(abstimmungid, **kwargs):
    """
    Aktualisiert die Details einer Abstimmung basierend auf der Abstimmungs-ID.
    Akzeptiert beliebige Spalten als Schlüsselwortargumente.
    """
    try:
        datenbank_verbindung_pruefen()

        if not kwargs:
            raise ValueError("Es wurden keine Felder zum Aktualisieren angegeben.")

        columns = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        values = list(kwargs.values()) + [abstimmungid]

        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()

            # Überprüfen, ob die Abstimmung existiert
            cursor.execute("SELECT COUNT(*) FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            if cursor.fetchone()[0] == 0:
                raise ValueError(f"Abstimmung mit ID {abstimmungid} existiert nicht.")

            # Aktualisieren der Abstimmung
            cursor.execute(f"UPDATE abstimmung SET {columns} WHERE abstimmungid = ?", values)
            conn.commit()

            logging.info(f"Abstimmung mit ID {abstimmungid} erfolgreich aktualisiert!")
    except sqlite3.Error as e:
        logging.error(f"Datenbankfehler bei der Aktualisierung der Abstimmung: {e}")
        raise
    except ValueError as e:
        logging.warning(f"Fehler: {e}")
        raise


def abstimmungEntfernen(abstimmungid):
    """
    Entfernt eine Abstimmung aus der Datenbank basierend auf der Abstimmungs-ID.
    """
    try:
        datenbank_verbindung_pruefen()

        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()

            # Überprüfen, ob die Abstimmung existiert
            cursor.execute("SELECT COUNT(*) FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            if cursor.fetchone()[0] == 0:
                raise ValueError(f"Abstimmung mit ID {abstimmungid} existiert nicht.")

            # Abstimmung löschen
            cursor.execute("DELETE FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            conn.commit()

            logging.info(f"Abstimmung mit ID {abstimmungid} erfolgreich entfernt!")
    except sqlite3.Error as e:
        logging.error(f"Datenbankfehler beim Entfernen der Abstimmung: {e}")
        raise
    except ValueError as e:
        logging.warning(f"Fehler: {e}")
        raise
