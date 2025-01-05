from Buerger import Buerger

class Stimme(Buerger):
    def __init__(self, buergerid, abstimmungid, entscheidung):
        super().__init__(buergerid)
        self.abstimmungid = abstimmungid
        self.entscheidung = entscheidung
