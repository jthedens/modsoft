from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.infrastructure.services.ErgebnisService import ErgebnisService
from src.main.python.evoting.infrastructure.repositories.ErgebnisRepository import ErgebnisRepository

class ErgebnisController:
    def __init__(self):
        self.service = ErgebnisService(ErgebnisRepository())

    def zeige_beendete_abstimmungen(self):
        """
        Ruft die beendeten Abstimmungen mit den Ergebnissen ab und übergibt sie an das Template.
        """
        return self.service.finde_beendete_abstimmungen()