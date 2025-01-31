from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.infrastructure.repositories.UserRepository import BuergerRepository
from src.main.python.evoting.infrastructure.services.PasswortService import hashPasswort
from datetime import datetime
import uuid
from ...domain.entities.Buerger import Buerger
import bcrypt  # Für Passwort-Hashing

class BuergerService:
    """
    Enthält die Geschäftslogik für die Entität 'Buerger'.
    Verwendet das Repository für Datenzugriff.
    """

    def __init__(self, repository):
        self.repository = repository

    #@log_method_call
    #@handle_exceptions
    def buerger_finden(self, email, passwort):
        """
        Findet einen Bürger anhand der E-Mail und überprüft das Passwort.
        :param email: Die E-Mail des Bürgers.
        :param passwort: Das eingegebene Passwort.
        :return: Ein Buerger-Objekt, wenn die Anmeldedaten korrekt sind.
        """
        buerger = self.repository.finde_buerger_nach_email(email)
        if not buerger:
            raise ValueError("Kein Benutzer gefunden.")

        # Validierung des eingegebenen Passworts mit dem gespeicherten Hash
        if not bcrypt.checkpw(passwort.encode('utf-8'), buerger.passwort):
            raise ValueError("Falsches Passwort.")
        return buerger

    @log_method_call
    @handle_exceptions
    def buerger_erstellen(self, vorname, nachname, geburtstag, adresse, plz, email, passwort):
        """
        Erstellt einen neuen Bürger und speichert ihn in der Datenbank.
        :param buergerid: Die eindeutige ID des Bürgers.
        :param vorname: Der Vorname des Bürgers.
        :param nachname: Der Nachname des Bürgers.
        :param geburtstag: Das Geburtsdatum des Bürgers.
        :param adresse: Die Adresse des Bürgers.
        :param plz: Die Postleitzahl des Bürgers.
        :param email: Die E-Mail des Bürgers.
        :param passwort: Das Passwort des Bürgers.
        :param rolle: Die Rolle des Bürgers.
        :param authentifizierungsstatus: Authentifizierungsstatus des Bürgers.
        """
        if self.repository.finde_buerger_nach_email(email):
            raise ValueError("Die E-Mail-Adresse existiert bereits!")

        # Passwort-Hashing
        hashed_passwort = hashPasswort(passwort)
        neuer_buerger = Buerger(str(uuid.uuid4()), vorname, nachname, geburtstag, adresse, plz, email, hashed_passwort, "Benutzer", 1)
        self.repository.speichere_buerger(neuer_buerger)

        return

    @log_method_call
    @handle_exceptions
    def finde_buerger_nach_email(self, email):
        # Aufruf der Repository-Methode, um den Bürger anhand der E-Mail zu finden
        return self.repository.finde_buerger_nach_email(email)


    @staticmethod
    def berechne_alter(geburtsdatum_str):
        # Das Geburtsdatum als String wird in ein datetime-Objekt umgewandelt
        geburtsdatum = datetime.strptime(geburtsdatum_str, "%Y-%m-%d")
        heute = datetime.today()

        # Alter berechnen
        alter = heute.year - geburtsdatum.year

        # Falls der Geburtstag in diesem Jahr noch nicht gewesen ist
        if (heute.month, heute.day) < (geburtsdatum.month, geburtsdatum.day):
            alter -= 1

        return alter