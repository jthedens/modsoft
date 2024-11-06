from datetime import datetime
from typing import List


class Bürger:
    def __init__(self, bürger_id: str, name: str, email: str, password: str, rolle: str, authentifizierungsstatus: bool, stimmberechtigung: bool):
        self.bürger_id = bürger_id
        self.name = name
        self.email = email
        self.password = password
        self.rolle = rolle
        self.authentifizierungsstatus = authentifizierungsstatus
        self.stimmberechtigung = stimmberechtigung

    def ist_stimmberechtigt(self) -> bool:
        return self.stimmberechtigung and self.authentifizierungsstatus


class Stimme:
    def __init__(self, bürger_id: str, abstimmungs_id: str, wahloption: str):
        self.bürger_id = bürger_id
        self.abstimmungs_id = abstimmungs_id
        self.wahloption = wahloption


class Abstimmung:
    def __init__(self, abstimmungs_id: str, titel: str, beschreibung: str, frist: datetime, abstimmungsstatus: bool):
        self.abstimmungs_id = abstimmungs_id
        self.titel = titel
        self.beschreibung = beschreibung
        self.frist = frist
        self.abstimmungsstatus = abstimmungsstatus
        self.verfügbare_optionen: List[str] = []

    def add_option(self, option: str):
        self.verfügbare_optionen.append(option)

    def ist_aktiv(self) -> bool:
        return self.abstimmungsstatus and datetime.now() <= self.frist

'''
class Organisation:
    def __init__(self, organisations_id: str, name: str, kontakt: str, authentifizierungsstatus: bool):
        self.organisations_id = organisations_id
        self.name = name
        self.kontakt = kontakt
        self.authentifizierungsstatus = authentifizierungsstatus
'''

# Beispiel für die Nutzung des Domain Models
if __name__ == "__main__":
    # Erstellen von Bürgern
    bürger1 = Bürger(bürger_id="B1", name="Max Mustermann", email="max@example.com", password="1234", rolle="buerger", authentifizierungsstatus=True, stimmberechtigung=True)
    bürger2 = Bürger(bürger_id="B2", name="Erika Mustermann", email="erika@example.com", password="1234", rolle="buerger",authentifizierungsstatus=True, stimmberechtigung=False)

    # Erstellen einer Organisation
    #organisation = Organisation(organisations_id="O1", name="Wahlorganisation", kontakt="kontakt@organisation.com", authentifizierungsstatus=True)

    # Erstellen einer Abstimmung
    abstimmung = Abstimmung(
        abstimmungs_id="A1",
        titel="Wahl 2024",
        beschreibung="Wählen Sie Ihren bevorzugten Kandidaten.",
        frist=datetime(2024, 12, 31),
        abstimmungsstatus=True,
    )

    # Optionen zur Abstimmung hinzufügen
    abstimmung.add_option("Kandidat A")
    abstimmung.add_option("Kandidat B")

    # Stimmen abgeben
    if bürger1.ist_stimmberechtigt():
        stimme1 = Stimme(bürger_id=bürger1.bürger_id, abstimmungs_id=abstimmung.abstimmungs_id, wahloption="Kandidat A")
        print(f"{bürger1.name} hat für {stimme1.wahloption} gestimmt.")
    else:
        print(f"{bürger1.name} ist nicht stimmberechtigt.")

    if bürger2.ist_stimmberechtigt():
        stimme2 = Stimme(bürger_id=bürger2.bürger_id, abstimmungs_id=abstimmung.abstimmungs_id, wahloption="Kandidat B")
        print(f"{bürger2.name} hat für {stimme2.wahloption} gestimmt.")
    else:
        print(f"{bürger2.name} ist nicht stimmberechtigt.")