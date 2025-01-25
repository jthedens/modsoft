from ...domain.entities.Buerger import Buerger
from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
import sqlite3
import os


class BuergerRepository:
    """
    Kapselt alle Datenbankoperationen für die Entität 'Buerger'.
    Trennt Datenbanklogik von der Geschäftslogik.
    """

    def __init__(self, db_path="eVoteMain.db"):
        if not os.path.exists(db_path):
            raise ValueError("Die Datenbankdatei existiert nicht!")
        self.db_path = db_path


    def finde_buerger_nach_email(self, email):
        """
        Sucht einen Bürger in der Datenbank anhand seiner E-Mail.
        :param email: Die E-Mail des zu suchenden Bürgers.
        :return: Ein Buerger-Objekt oder None, wenn nicht gefunden.
        """
        query = """
            SELECT buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus
            FROM buerger WHERE email = ?
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (email,)).fetchone()
            if result:
                # Erstellen eines Buerger-Objekts aus den Ergebnissen
                return Buerger(*result)
            return None

    @log_method_call
    @handle_exceptions
    def speichere_buerger(self, buerger):
        """
        Speichert einen neuen Bürger in der Datenbank.
        :param buerger: Ein Buerger-Objekt, das gespeichert werden soll.
        """
        query = """
            INSERT INTO buerger (buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (
                buerger.buergerid, buerger.vorname, buerger.nachname, buerger.geburtstag,
                buerger.adresse, buerger.plz, buerger.email, buerger.passwort, buerger.rolle, buerger.authentifizierungsstatus
            ))
            conn.commit()

