from Buerger import Buerger

class Stimme(Buerger):
    def __init__(self, buergerid, abstimmungid, stimme):
        super().__init__(buergerid)
        self.abstimmungid = abstimmungid
        self.stimme = stimme
