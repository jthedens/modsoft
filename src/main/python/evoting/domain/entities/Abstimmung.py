from datetime import datetime

class Abstimmung:
    def __init__(self, abstimmungid, titel, beschreibung, frist, altersgrenze, status):
        self.abstimmungid = abstimmungid
        self.titel = titel
        self.beschreibung = beschreibung
        self.frist = frist
        self.altersgrenze = altersgrenze
        self.status = status

    def ist_verfuegbar(self):
        """
        Prüft, ob die Abstimmung verfügbar ist (z. B. basierend auf der Frist).
        :return: True, wenn die Abstimmung verfügbar ist, sonst False
        """
        return datetime.now() <= self.frist