import sqlite3
from abstimmung_domain import Abstimmung

class AbstimmungRepository:
    def existiert(self, abstimmungid):
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            return cursor.fetchone()[0] > 0

    def speichern(self, abstimmung: Abstimmung):
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            if self.existiert(abstimmung.abstimmungid):
                cursor.execute("""
                    UPDATE abstimmung
                    SET titel = ?, beschreibung = ?, frist = ?, altersgrenze = ?, status = ?
                    WHERE abstimmungid = ?
                """, (abstimmung.titel, abstimmung.beschreibung, abstimmung.frist.strftime("%Y-%m-%d"),
                      abstimmung.altersgrenze, abstimmung.status, abstimmung.abstimmungid))
            else:
                cursor.execute("""
                    INSERT INTO abstimmung (abstimmungid, titel, beschreibung, frist, altersgrenze, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (abstimmung.abstimmungid, abstimmung.titel, abstimmung.beschreibung,
                      abstimmung.frist.strftime("%Y-%m-%d"), abstimmung.altersgrenze, abstimmung.status))
            conn.commit()

    def finde_nach_id(self, abstimmungid):
        with sqlite3.connect("eVoteMain.db") as conn:
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
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM abstimmung WHERE abstimmungid = ?", (abstimmungid,))
            conn.commit()

    def hole_abstimmungen(self):
        """
        Holt alle Abstimmungen aus der Datenbank.
        :return: Eine Liste von Abstimmungen
        """
        # Beispiel für das Abrufen aus einer SQLite-Datenbank:
        daten = []
        with sqlite3.connect("eVoteMain.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT abstimmungid, titel, beschreibung, frist, altersgrenze, status 
                FROM abstimmung
            """)
            result = cursor.fetchall()
            for row in result:
                daten.append({
                    "abstimmungid": row[0],
                    "titel": row[1],
                    "beschreibung": row[2],
                    "frist": row[3],
                    "altersgrenze": row[4],
                    "status": row[5]
                })
            return daten