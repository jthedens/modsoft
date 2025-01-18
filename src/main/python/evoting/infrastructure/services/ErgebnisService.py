from src.main.python.evoting.infrastructure.services.AbstimmungsService import AbstimmungService
from src.main.python.evoting.infrastructure.repositories.AbstimmungRepository import AbstimmungRepository

class ErgebnisService:
    def __init__(self, repository):
        self.repository = repository
        self.abstimmung_service = AbstimmungService(AbstimmungRepository())

    def finde_beendete_abstimmungen(self):
        # Hole alle Abstimmungen aus dem Repository
        alle_abstimmungen = self.abstimmung_service.finde_alle_abstimmungen()

        # Filtere beendete Abstimmungen
        beendete_abstimmungen = [
            {
                "abstimmungid": abstimmung.abstimmungid,
                "titel": abstimmung.titel,
                "ergebnis": self.repository.hole_ergebnis(abstimmung.abstimmungid)
            }
            for abstimmung in alle_abstimmungen
            if abstimmung.status == 0
        ]

        return beendete_abstimmungen