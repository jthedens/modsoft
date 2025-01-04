from datetime import datetime

class Buerger:
    def __init__(self, buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus):
        self.buergerid = buergerid
        self.vorname = vorname
        self.nachname = nachname
        # Validierung des Datumsformats
        try:
            datetime.strptime(geburtstag, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Ungültiges Datumsformat: {geburtstag}. Erwartet: YYYY-MM-DD")
        self.geburtstag = geburtstag
        self.adresse = adresse
        self.plz = plz
        self.email = email
        self.passwort = passwort
        self.rolle = rolle
        self.authentifizierungsstatus = authentifizierungsstatus

    def voller_name(self):
        return f"{self.vorname} {self.nachname}"

    def ist_authentifiziert(self):
        return self.authentifizierungsstatus == "aktiv"

    def berechne_alter(self):
        geburtsdatum_dt = datetime.strptime(self.geburtstag, "%Y-%m-%d")
        heute = datetime.now()
        alter = heute.year - geburtsdatum_dt.year
        if (heute.month, heute.day) < (geburtsdatum_dt.month, geburtsdatum_dt.day):
            alter -= 1
        return alter