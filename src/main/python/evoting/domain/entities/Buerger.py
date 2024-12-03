class Citizen:
    def __init__(self, citizen_id, name, email, password, role, authentifizierungsstatus, stimmberechtigung):
        self.citizen_id = citizen_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.authentifizierungsstatus = authentifizierungsstatus
        self.stimmberechtigung = stimmberechtigung
