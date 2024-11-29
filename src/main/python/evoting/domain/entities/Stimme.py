from Buerger import Citizens

class Stimme(Citizens):
    def __init__(self, citizens_id, name, email, password, rolle, authentifizierungsstatus, stimmberechtigung,
                 wahloption):
        super().__init__(citizens_id, name, email, password, rolle, authentifizierungsstatus, stimmberechtigung)
        #self.abstimmungs_id = abstimmungs_id
        self.wahloption = wahloption
