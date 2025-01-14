from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.domain.entities.Abstimmung import Abstimmung
import logging

class AbstimmungService:
    @log_method_call
    @handle_exceptions
    def __init__(self, repository):
        self.repository = repository
        self.logger = logging.getLogger(__name__)

    @log_method_call
    @handle_exceptions
    def erstelle_abstimmung(self, abstimmung: Abstimmung):
        if self.repository.existiert(abstimmung.abstimmungid):
            self.logger.warning(f"Abstimmung mit ID {abstimmung.abstimmungid} existiert bereits.")
            raise ValueError(f"Abstimmung mit ID {abstimmung.abstimmungid} existiert bereits.")
        self.repository.speichern(abstimmung)
        self.logger.info(f"Abstimmung {abstimmung.abstimmungid} erstellt.")

    @log_method_call
    @handle_exceptions
    def finde_abstimmung(self, abstimmungid):
        abstimmung = self.repository.finde_nach_id(abstimmungid)
        if not abstimmung:
            raise ValueError(f"Abstimmung mit ID {abstimmungid} nicht gefunden.")
        return abstimmung

    @log_method_call
    @handle_exceptions
    def aktualisiere_abstimmung(self, abstimmungid, **kwargs):
        abstimmung = self.finde_abstimmung(abstimmungid)
        abstimmung.aktualisieren(**kwargs)
        self.repository.speichern(abstimmung)

    @log_method_call
    @handle_exceptions
    def entferne_abstimmung(self, abstimmungid):
        abstimmung = self.finde_abstimmung(abstimmungid)
        self.repository.entfernen(abstimmungid)

    @log_method_call
    @handle_exceptions
    def finde_alle_abstimmungen(self):
        """
        Holt alle Abstimmungen aus der Datenbank.
        :return: Eine Liste von Abstimmungen
        """
        return self.repository.hole_abstimmungen()

    @log_method_call
    @handle_exceptions
    def pruefe_buerger_hat_abgestimmt(self, abstimmungid, buergerid):
        """
        Prüft, ob der Bürger bereits für eine Abstimmung abgestimmt hat.
        """
        return self.repository.buerger_hat_abgestimmt(abstimmungid, buergerid)

    #@log_method_call
    #@handle_exceptions
    def abstimmen(self, abstimmungid, buergerid, stimme):
        """
        Ermöglicht einem Bürger die Teilnahme an einer Abstimmung.
        """
        print('ist im service')
        if self.repository.buerger_hat_abgestimmt(abstimmungid, buergerid):
            print('error')
            raise ValueError("Der Bürger hat bereits abgestimmt.")
        print('kein error')
        self.repository.speichere_stimme(abstimmungid, buergerid, stimme)
