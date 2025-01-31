from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.infrastructure.services.UserService import BuergerService
from src.main.python.evoting.infrastructure.repositories.UserRepository import BuergerRepository
from src.main.python.evoting.domain.entities.Buerger import Buerger

class BuergerController:
    """
    Schnittstelle für die Außenwelt, z. B. Webanwendungen oder APIs.
    Ruft die Geschäftslogik im Service auf und formatiert die Ergebnisse.
    """

    def __init__(self):
        self.service = BuergerService(BuergerRepository())

    #@log_method_call
    #@handle_exceptions
    def finde_buerger(self, email, passwort):
        """
        Sucht einen Bürger und gibt die Ergebnisse in einem lesbaren Format zurück.
        :param email: Die E-Mail des Bürgers.
        :param passwort: Das eingegebene Passwort.
        :return: Ein Dictionary mit den Bürgerinformationen oder einer Fehlermeldung.
        """
        try:
            buerger = self.service.buerger_finden(email, passwort)
            return {
                "buergerid": buerger.buergerid,
                "voller_name": buerger.voller_name(),
                "email": buerger.email,
                "rolle": buerger.rolle,
                "authentifizierungsstatus": buerger.ist_authentifiziert()
            }
        except Exception as e:
            return {"error": str(e)}

    @log_method_call
    @handle_exceptions
    def erstelle_buerger(self, vorname, nachname, geburtstag, adresse, plz, email, passwort):
        """
        Erstellt einen neuen Bürger und gibt eine Bestätigung oder Fehlermeldung zurück.
        :param buergerid: Die eindeutige ID des Bürgers.
        :param vorname: Der Vorname des Bürgers.
        :param nachname: Der Nachname des Bürgers.
        :param geburtstag: Das Geburtsdatum des Bürgers.
        :param adresse: Die Adresse des Bürgers.
        :param plz: Die Postleitzahl des Bürgers.
        :param email: Die E-Mail-Adresse des Bürgers.
        :param passwort: Das Passwort des Bürgers.
        :param rolle: Die Rolle des Bürgers.
        :param authentifizierungsstatus: Der Authentifizierungsstatus.
        :return: Ein Dictionary mit einer Bestätigung oder einer Fehlermeldung.
        """
        print("erstelle Bürger")
        try:
            self.service.buerger_erstellen(
                vorname=vorname,
                nachname=nachname,
                geburtstag=geburtstag,
                adresse=adresse,
                plz=plz,
                email=email,
                passwort=passwort
            )
            return {"success": "Bürger wurde erfolgreich erstellt."}
        except Exception as e:
            return {"error": str(e)}
