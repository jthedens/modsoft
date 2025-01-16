from src.main.python.evoting.application.dekoratoren.dekoratoren import log_method_call, handle_exceptions
from src.main.python.evoting.infrastructure.services.ErgebnisService import ErgebnisService
from src.main.python.evoting.infrastructure.repositories.ErgebnisRepository import ErgebnisRepository


class ErgebnisController:
    """
    Schnittstelle für die Außenwelt, z. B. Webanwendungen oder APIs.
    Ruft die Geschäftslogik im Service auf und formatiert die Ergebnisse.
    """

    def __init__(self):
        self.service = ErgebnisService(ErgebnisRepository())



    @log_method_call
    @handle_exceptions
    def finde_verfuegbare_ergebnisse(self, buergerid):
        """
        Ruft die Ergebnisse aller Abstimmungen ab, an denen der Bürger abstimmen kann,
        und deren Status 'offen' (0) ist.

        :param buergerid: Die ID des Bürgers.
        :return: Eine Liste von Abstimmungen mit Ergebnissen oder eine Fehlermeldung.
        """
        try:
            # Abrufen der offenen Abstimmungen, an denen der Bürger teilnehmen kann
            abstimmungen = self.service.finde_offene_abstimmungen(buergerid)
            verfuegbare_ergebnisse = []

            for abstimmung in abstimmungen:
                if abstimmung.status == 0:  # Status prüfen (offen)
                    ergebnis = self.service.finde_ergebnis(abstimmung.abtsimmungid)
                    verfuegbare_ergebnisse.append({
                        "abstimmungid": abstimmung.id,
                        "titel": abstimmung.titel,
                        "status": abstimmung.status,
                        "ergebnis": ergebnis,
                    })

            return {"status": "success", "ergebnisse": verfuegbare_ergebnisse}

        except Exception as e:
            self.logger.error(f"Fehler beim Abrufen der verfügbaren Ergebnisse: {e}")
            return {"status": "failure", "error": str(e)}



    @log_method_call
    @handle_exceptions
    def finde_ergebnis(self, abstimmungid, stimme):
        """
        Ruft das Ergebnis für eine bestimmte Abstimmung ab.
        :param abstimmungid: Die ID der Abstimmung.
        :param stimme: Die spezifische Stimme, deren Ergebnis abgerufen wird.
        :return: Das Ergebnis als Dictionary oder Fehlernachricht.
        """
        try:
            ergebnis = self.service.finde_ergebnis(abstimmungid, stimme)
            return {"status": "success", "ergebnis": ergebnis}
        except Exception as e:
            self.logger.error(f"Fehler beim Abrufen des Ergebnisses: {e}")
            return {"status": "failure", "error": str(e)}

    @log_method_call
    @handle_exceptions
    def erstelle_ergebnis(self, abstimmungid, stimmen_verteilung):
        """
        Erstellt oder aktualisiert ein Ergebnis für eine Abstimmung.
        :param abstimmungid: Die ID der Abstimmung.
        :param stimmen_verteilung: Die Verteilung der Stimmen, die gespeichert werden soll.
        :return: Statusnachricht über Erfolg oder Fehler.
        """
        try:
            self.service.erstelle_ergebnis(abstimmungid, stimmen_verteilung)
            return {"status": "success", "message": "Ergebnis erfolgreich erstellt oder aktualisiert."}
        except Exception as e:
            self.logger.error(f"Fehler beim Erstellen des Ergebnisses: {e}")
            return {"status": "failure", "error": str(e)}
