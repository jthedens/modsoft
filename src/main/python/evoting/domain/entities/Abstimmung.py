from datetime import datetime

class Abstimmung:
    def __init__(self, abstimmungs_id: str, titel: str, beschreibung: str, frist: datetime, abstimmungsstatus: bool):
        self.abstimmungs_id = abstimmungs_id
        self.titel = titel
        self.beschreibung = beschreibung
        self.frist = frist
        self.abstimmungsstatus = abstimmungsstatus
        self.verfuegbare_optionen: List[str] = []