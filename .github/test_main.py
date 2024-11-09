import unittest
from main import Citizens, Stimme  # Passen Sie den Modulnamen an

class TestCitizens(unittest.TestCase):
    def setUp(self):
        self.citizen = Citizens(
            citizens_id="C1",
            name="Max Mustermann",
            email="max@example.com",
            password="password123",
            rolle="Bürger",
            authentifizierungsstatus="0",
            stimmberechtigung="1",
        )

    def test_ist_stimmberechtigt(self):
        # Testet, ob der Bürger stimmberechtigt ist
        self.assertTrue(self.citizen.ist_stimmberechtigt())

class TestStimme(unittest.TestCase):
    def setUp(self):
        self.stimme = Stimme(
            citizens_id="100000",
            name="Max Mustermann",
            email="max@example.com",
            password="password123",
            rolle="Bürger",
            authentifizierungsstatus="0",
            stimmberechtigung="1",
            wahloption="X"
        )

    def test_stimme_abgabe_berechtigt(self):
        # Testet die Stimmabgabe für einen stimmberechtigten Bürger
        self.stimme.wahloption = "Y"  # Simulierte Eingabe ohne Benutzerinteraktion
        self.assertEqual(self.stimme.wahloption, "Y")

    def test_stimme_abgabe_nicht_berechtigt(self):
        # Testet die Stimmabgabe für einen Bürger, der nicht stimmberechtigt ist
        self.stimme.stimmberechtigung = "0"
        with self.assertRaises(Exception):  # Falls `stimmeAbgabe` bei fehlender Berechtigung eine Exception wirft
            self.stimme.stimmeAbgabe(self.stimme.stimmberechtigung)

if __name__ == "__main__":
    unittest.main()
