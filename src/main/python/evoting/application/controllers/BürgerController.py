from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.infrastructure.services.UserService import BuergerService
from src.main.python.evoting.infrastructure.repositories.UserRepository import BuergerRepository

class BuergerController:
    """
    Schnittstelle für die Außenwelt, z. B. Webanwendungen oder APIs.
    Ruft die Geschäftslogik im Service auf und formatiert die Ergebnisse.
    """

    @log_method_call
    @handle_exceptions
    def __init__(self):
        self.service = BuergerService(BuergerRepository())

    @log_method_call
    @handle_exceptions
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
