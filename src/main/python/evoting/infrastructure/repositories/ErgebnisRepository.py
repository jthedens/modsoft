from src.main.python.evoting.domain.entities.Abstimmung import Abstimmung
from src.main.python.evoting.domain.entities.Ergebnis import Ergebnis
import sqlite3
import os

class ErgebnisRepository:
    def __init__(self, db_path="eVoteMain.db"):
        if not os.path.exists(db_path):
            raise ValueError("Die Datenbankdatei existiert nicht!")
        self.db_path = db_path

    def hole_ergebnis(self, abstimmungid):
        """
        Holt das Ergebnis einer bestimmten Abstimmung aus der Datenbank.
        :param abstimmungid: Die ID der Abstimmung, deren Ergebnis abgerufen wird.
        :return: Ein Ergebnis-Objekt
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Zähle die Stimmen für die Abstimmung
            cursor.execute("""
                SELECT stimme, COUNT(*) AS anzahl
                FROM auswertung
                WHERE abstimmungid = ?
                GROUP BY stimme
            """, (abstimmungid,))

            ergebnisse = cursor.fetchall()

        # Initialisieren der Zähler für Ja und Nein
        ja_anzahl = 0
        nein_anzahl = 0

        # Zähle die Ja und Nein Stimmen
        for stimme, anzahl in ergebnisse:
            if stimme.lower() == "ja":
                ja_anzahl = anzahl
            elif stimme.lower() == "nein":
                nein_anzahl = anzahl

        # Erstelle das Ergebnis-Objekt
        return Ergebnis(abstimmungid, ja_anzahl, nein_anzahl)

