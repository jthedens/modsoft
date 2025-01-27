import unittest
from src.main.python.evoting.domain.entities.Ergebnis import Ergebnis

class TestErgebnis(unittest.TestCase):
    def test_ergebnis_berechnung(self):
        """
        Testet, ob die Berechnungen für ja_prozent und nein_prozent korrekt sind.
        """
        ergebnis = Ergebnis(abstimmungid=1, ja_anzahl=80, nein_anzahl=20)
        self.assertEqual(ergebnis.ja_prozent, 80.0)
        self.assertEqual(ergebnis.nein_prozent, 20.0)
        self.assertEqual(ergebnis.gesamt_stimmen, 100)

    def test_ergebnis_leer(self):
        """
        Testet den Fall, dass keine Stimmen abgegeben wurden.
        """
        ergebnis = Ergebnis(abstimmungid=2, ja_anzahl=0, nein_anzahl=0)
        self.assertEqual(ergebnis.ja_prozent, 0.0)
        self.assertEqual(ergebnis.nein_prozent, 0.0)
        self.assertEqual(ergebnis.gesamt_stimmen, 0)

    def test_ergebnis_str_representation(self):
        """
        Testet die String-Repräsentation des Ergebnisses.
        """
        ergebnis = Ergebnis(abstimmungid=3, ja_anzahl=25, nein_anzahl=75)
        self.assertEqual(str(ergebnis), "Ja: 25.0%, Nein: 75.0%")

    def test_ergebnis_mixed(self):
        """
        Testet ein gemischtes Abstimmungsergebnis.
        """
        ergebnis = Ergebnis(abstimmungid=4, ja_anzahl=45, nein_anzahl=55)
        self.assertEqual(ergebnis.ja_prozent, 45.0)
        self.assertEqual(ergebnis.nein_prozent, 55.0)
        self.assertEqual(ergebnis.gesamt_stimmen, 100)

if __name__ == "__main__":
    unittest.main()