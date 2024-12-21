import bcrypt  # Für Passwort-Hashing
import os
import sqlite3

def burgerErstellen(buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus):
    try:
        # Überprüfen, ob die Datenbankdatei existiert
        if not os.path.exists("eVoteMain.db"):
            raise ValueError("Die Datenbankdatei existiert nicht!")

        # Verbindung zur Datenbank mit 'with', um automatische Schließung sicherzustellen
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()

            # Überprüfen, ob die E-Mail bereits in der Datenbank existiert
            cursor.execute("SELECT COUNT(*) FROM buerger WHERE email = ?", (email,))
            if cursor.fetchone()[0] > 0:
                raise ValueError("Die E-Mail-Adresse existiert bereits!")

            # Passwort-Hashing
            hashed_passwort = hashPasswort(passwort)

            # Datensatz in die Tabelle 'buerger' einfügen
            cursor.execute("""
            INSERT INTO buerger (
                buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                buergerid,  # ID des Bürgers
                vorname,  # Vorname
                nachname,  # Nachname
                geburtstag,  # Geburtsdatum
                adresse,  # Adresse
                plz,  # Postleitzahl
                email,  # E-Mail-Adresse
                hashed_passwort,  # Gehashtes Passwort
                rolle,  # Rolle
                authentifizierungsstatus  # Authentifizierungsstatus (1 = authentifiziert)
            ))

            # Änderungen in der Datenbank übernehmen
            conn.commit()

            print("Bürger erfolgreich erstellt!")
    except sqlite3.Error as e:
        raise Exception(f"Fehler beim Hinzufügen zur Datenbank: {e}")
    except ValueError as ve:
        raise Exception(f"Fehler: {ve}")
    except Exception as ex:
        raise Exception(f"Unerwarteter Fehler: {ex}")

# Funktion zum Erstellen eines gehashten Passworts
def hashPasswort(passwort):
    try:
        # Generiere ein Salt
        salt = bcrypt.gensalt()
        # Hash das Passwort mit dem Salt
        hashed_passwort = bcrypt.hashpw(passwort.encode('utf-8'), salt)
        return hashed_passwort
    except Exception as e:
        raise Exception(f"Fehler beim Hashen des Passworts: {e}")



# Funktion zum Löschen eines Bürgers (noch nicht implementiert)
def buergerEntfernen(buergerid):
    try:
        # Überprüfen, ob die Datenbankdatei existiert
        if not os.path.exists("eVoteMain.db"):
            raise ValueError("Die Datenbankdatei existiert nicht!")

        # Verbindung zur Datenbank mit 'with', um automatische Schließung sicherzustellen
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()

            # Überprüfen, ob der Bürger mit der gegebenen ID existiert
            cursor.execute("SELECT COUNT(*) FROM buerger WHERE buergerid = ?", (buergerid,))
            if cursor.fetchone()[0] == 0:
                raise ValueError("Kein Bürger mit dieser ID gefunden!")

            # Bürger aus der Datenbank löschen
            cursor.execute("DELETE FROM buerger WHERE buergerid = ?", (buergerid,))

            # Änderungen in der Datenbank übernehmen
            conn.commit()

            print(f"Bürger mit der ID {buergerid} wurde erfolgreich gelöscht!")
    except sqlite3.Error as e:
        raise Exception(f"Fehler beim Löschen des Bürgers: {e}")
    except ValueError as ve:
        raise Exception(f"Fehler: {ve}")
    except Exception as ex:
        raise Exception(f"Unerwarteter Fehler: {ex}")