from src.main.python.evoting.domain.entities.Stimme import Buerger
import sqlite3
import bcrypt  # Für Passwort-Hashing
import os

def findeBuerger(email, passwort):
    try:
        # Zugriff auf die Datenbank mit 'with', um automatische Verbindungsschließung sicherzustellen

        if not os.path.exists("eVoteMain.db"):
            raise ValueError("Die Datenbankdatei existiert nicht!")

        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            # SQL-Abfrage ausführen
            cursor.execute(
                """SELECT 
                    buergerid, 
                    vorname,
                    nachname, 
                    geburtstag, 
                    adresse, 
                    plz, 
                    email, 
                    passwort, 
                    rolle, 
                    authentifizierungsstatus
                FROM buerger 
                WHERE email = ?""",  # Wir prüfen nur nach Email, weil Passwörter nie im Klartext in der DB gespeichert werden sollten.
                (email,)
            )

            # Einträge aus der Datenbank abholen
            result = cursor.fetchone()

            if result is None:
                raise ValueError("Kein Benutzer gefunden. Ungültige Email oder Passwort.")

            # Entpacken der Ergebnisse
            buergerid, vorname, nachname, geburtstag, adresse, plz, email, hashed_password, rolle, authentifizierungsstatus = result

            print(hashed_password)

            # Passwort mit dem gehashten Passwort vergleichen
            if not bcrypt.checkpw(passwort.encode('utf-8'), hashed_password):
                raise ValueError("Falsches Passwort.")

            # Rückgabe der Benutzerinformationen
            return {
                "buergerid": buergerid,
                "voller_name": f"{vorname} {nachname}",
                "email": email,
                "rolle": rolle,
                "authentifizierungsstatus": authentifizierungsstatus,
                "geburtstag": geburtstag,
                "adresse": adresse,
                "plz": plz
            }

    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        raise
    except ValueError as e:
        print(f"Fehler: {e}")
        raise

