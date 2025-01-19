class Ergebnis:
    def __init__(self, abstimmungid, ja_anzahl, nein_anzahl):
        self.abstimmungid = abstimmungid
        self.ja_anzahl = ja_anzahl
        self.nein_anzahl = nein_anzahl
        self.gesamt_stimmen = ja_anzahl + nein_anzahl
        self.ja_prozent = (ja_anzahl / self.gesamt_stimmen) * 100 if self.gesamt_stimmen > 0 else 0
        self.nein_prozent = (nein_anzahl / self.gesamt_stimmen) * 100 if self.gesamt_stimmen > 0 else 0

    def __str__(self):
        return f"Ja: {self.ja_prozent:.1f}%, Nein: {self.nein_prozent:.1f}%"