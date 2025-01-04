class AbstimmungService:
    def __init__(self, repository):
        self.repository = repository

    def erstelle_abstimmung(self, abstimmung: Abstimmung):
        if self.repository.existiert(abstimmung.abstimmungid):
            raise ValueError(f"Abstimmung mit ID {abstimmung.abstimmungid} existiert bereits.")
        self.repository.speichern(abstimmung)

    def finde_abstimmung(self, abstimmungid):
        abstimmung = self.repository.finde_nach_id(abstimmungid)
        if not abstimmung:
            raise ValueError(f"Abstimmung mit ID {abstimmungid} nicht gefunden.")
        return abstimmung

    def aktualisiere_abstimmung(self, abstimmungid, **kwargs):
        abstimmung = self.finde_abstimmung(abstimmungid)
        abstimmung.aktualisieren(**kwargs)
        self.repository.speichern(abstimmung)

    def entferne_abstimmung(self, abstimmungid):
        abstimmung = self.finde_abstimmung(abstimmungid)
        self.repository.entfernen(abstimmungid)

    def finde_alle_abstimmungen(self):
        """
        Holt alle Abstimmungen aus der Datenbank.
        :return: Eine Liste von Abstimmungen
        """
        return self.repository.hole_abstimmungen()
