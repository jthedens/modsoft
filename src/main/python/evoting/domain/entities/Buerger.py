class Buerger:
    def __init__(self, buergerid, name, email, geburtstag, adresse, plz, password, rolle, authentifizierungsstatus):
        self.buergerid = buergerid
        self.name = name
        self.geburtstag = geburtstag
        self.adresse = adresse
        self.plz = plz
        self.email = email
        self.password = password
        self.rolle = rolle
        self.authentifizierungsstatus = authentifizierungsstatus
