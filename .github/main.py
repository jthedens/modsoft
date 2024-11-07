from cgi import print_environ
from datetime import datetime
from typing import List
import sqlite3

class Citizens:
    def __init__(self, citizens_id, name, email, password, rolle, authentifizierungsstatus, stimmberechtigung):
        self.citizens_id = citizens_id
        self.name = name
        self.email = email
        self.password = password
        self.rolle = rolle
        self.authentifizierungsstatus = authentifizierungsstatus
        self.stimmberechtigung = stimmberechtigung

    def ist_stimmberechtigt(self) -> bool:
        return self.stimmberechtigung and self.authentifizierungsstatus


'''
class Organisation:
    def __init__(self, organisations_id: str, name: str, kontakt: str, authentifizierungsstatus: bool):
        self.organisations_id = organisations_id
        self.name = name
        self.kontakt = kontakt
        self.authentifizierungsstatus = authentifizierungsstatus
'''



class Stimme(Citizens):
    def __init__(self, citizens_id,  name, email, password, rolle, authentifizierungsstatus, stimmberechtigung, wahloption):
        super().__init__(citizens_id,  name, email, password, rolle, authentifizierungsstatus, stimmberechtigung)
        #self.abstimmungs_id = abstimmungs_id
        self.wahloption = wahloption

    def stimmeAbgabe(self, stimmberechtigung):
        if stimmberechtigung == True:

            self.wahloption = input("Abstimmen (Y/N): ")
            if self.wahloption == "Y":
                print(f"{self.name} hat für {self.wahloption} gestimmt.")
                # Eintrag in Datenbank Stimme, Eintrag in Datenbank Bürger - ändern der Stimmberechtigung

            elif self.wahloption == "N":
                print(f"{self.name} hat für {self.wahloption} gestimmt.")
                # Eintrag in Datenbank Stimme, Eintrag in Datenbank Bürger - ändern der Stimmberechtigung
            else:
                print("ERROR in der Stimmenabgabe")

        else:
            print(f"{self.name} ist nicht stimmberechtigt.")




'''
        if bürger2.ist_stimmberechtigt():
            stimme2 = Stimme(bürger_id=bürger2.bürger_id, abstimmungs_id=abstimmung.abstimmungs_id,
                             wahloption="Kandidat B")
            print(f"{bürger2.name} hat für {stimme2.wahloption} gestimmt.")
        else:
            print(f"{bürger2.name} ist nicht stimmberechtigt.")
'''


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


def callCitizens():
    citizens_mail = input("E-Mail: ")
    citizens_password = input("Password: ")

    res = cursor.execute("SELECT CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED FROM CITIZENS WHERE EMAIL = ? AND PASSWORD = ?",(citizens_mail, citizens_password))
    CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED = res.fetchone()

    '''
    if citizens1.authentifizierungsstatus == "0":
        authentifizierungsStatusChange = input("Authentifizieren? (Y/N): ")

        if authentifizierungsStatusChange == "Y":
            updateAuthentifizierungsStatus = "UPDATE CITIZENS SET AUTHENTICATIONSTATUS = ? WHERE CITIZENSID = ?"
            resUpdate = cursor.execute(updateAuthentifizierungsStatus, ("1", citizens1.citizens_id))

        else:
            print("ERROR")
    '''

    return CITIZENSID, FIRSTNAME + " " + LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED


# Beispiel für die Nutzung des Domain Models
if __name__ == "__main__":

    #Zugriff auf die Datenbank
    conn = sqlite3.connect('citizens.db')
    #Cursor erstellen
    cursor = conn.cursor()

    # Erstellen von Bürgern
    dataCitizens = callCitizens()
    citizens1 = Citizens(dataCitizens[0], dataCitizens[1], dataCitizens[2], dataCitizens[3], dataCitizens[4], dataCitizens[5], dataCitizens[6])
    # Stimmen abgeben
    stimme1 = Stimme(citizens1.citizens_id, citizens1.name, citizens1.email, citizens1.password, citizens1.rolle, citizens1.authentifizierungsstatus, citizens1.stimmberechtigung, wahloption = "X")
    stimme1.stimmeAbgabe(citizens1.stimmberechtigung)
    #bürger2 = Bürger(bürger_id="B2", name="Erika Mustermann", email="erika@example.com", password="1234", rolle="buerger",authentifizierungsstatus=True, stimmberechtigung=False)

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


    # Commit your changes in the database
    conn.commit()
    # Closing the connection
    conn.close()