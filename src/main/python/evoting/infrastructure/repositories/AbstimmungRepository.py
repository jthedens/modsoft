import sqlite3
import os
from datetime import datetime

from src.main.python.evoting.application.dekoratoren.dekoratoren import handle_exceptions, log_method_call
from src.main.python.evoting.domain.entities.Abstimmung import Abstimmung

class AbstimmungRepository:

    def __init__(self, db_path="eVoteMain.db"):
        if not os.path.exists(db_path):
            raise ValueError("Die Datenbankdatei existiert nicht!")
        self.db_path = db_path

    def existiert(self, abstimmungid):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            return cursor.fetchone()[0] > 0

    import uuid
    from datetime import datetime

    def speichern(self, abstimmung):
        """
        Speichert eine Abstimmung in der Datenbank. Falls die Abstimmung existiert, wird sie aktualisiert.
        Falls keine ID vorhanden ist, wird eine neue UUID generiert.
        :param abstimmung: Ein Abstimmungsobjekt
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Überprüfen, ob die Abstimmung bereits existiert
            if not abstimmung.abstimmungid:
                # Generiere eine neue UUID, wenn die ID nicht vorhanden ist
                abstimmung.abstimmungid = str(uuid.uuid4())

            if self.existiert(abstimmung.abstimmungid):
                # Abstimmung existiert bereits, aktualisieren
                cursor.execute("""
                    UPDATE abstimmung
                    SET titel = ?, beschreibung = ?, frist = ?, altersgrenze = ?, status = ?
                    WHERE abstimmungid = ?
                """, (
                    abstimmung.titel,
                    abstimmung.beschreibung,
                    abstimmung.frist.strftime("%Y-%m-%d") if isinstance(abstimmung.frist, datetime) else abstimmung.frist,
                    abstimmung.altersgrenze,
                    abstimmung.status,
                    abstimmung.abstimmungid
                ))
            else:
                # Neue Abstimmung einfügen
                cursor.execute("""
                    INSERT INTO abstimmung (abstimmungid, titel, beschreibung, frist, altersgrenze, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    abstimmung.abstimmungid,
                    abstimmung.titel,
                    abstimmung.beschreibung,
                    abstimmung.frist.strftime("%y-%m-%d") if isinstance(abstimmung.frist,datetime) else abstimmung.frist,
                    abstimmung.altersgrenze,
                    abstimmung.status
                ))

            conn.commit()

    def finde_nach_id(self, abstimmungid):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT abstimmungid, titel, beschreibung, frist, altersgrenze, status
                FROM abstimmung WHERE abstimmungid = ?
            """, (abstimmungid,))
            row = cursor.fetchone()
            if row:
                return Abstimmung(*row)
            return None

    def entfernen(self, abstimmungid):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            conn.commit()

    @log_method_call
    @handle_exceptions
    def hole_abstimmungen(self):
        """
        Holt alle Abstimmungen aus der Datenbank.
        :return: Eine Liste von Abstimmungen
        """
        daten = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT abstimmungid, titel, beschreibung, frist, altersgrenze, status
                FROM abstimmung
            """)
            result = cursor.fetchall()
            for row in result:
                daten.append({
                    "abstimmungid": row[0],  # Die zufällige ID
                    "titel": row[1],
                    "beschreibung": row[2],
                    "frist": row[3],
                    "altersgrenze": row[4],
                    "status": row[5]
                })
        return daten

    def buerger_hat_abgestimmt(self, abstimmungid, buergerid):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM auswertung WHERE abstimmungid = ? AND buergerid = ?",
                (abstimmungid, buergerid)
            )
            return cursor.fetchone()[0] > 0

    def speichere_stimme(self, abstimmungid, buergerid, stimme):
        print('ist in repo')
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO auswertung(abstimmungid, buergerid, stimme) VALUES (?, ?, ?)",
                (abstimmungid, buergerid, stimme)
            )
            conn.commit()