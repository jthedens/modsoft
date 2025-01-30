import unittest
from datetime import datetime
from Buerger import Buerger  # Ersetze 'your_module_name' durch den tatsächlichen Modulnamen.


class TestBuerger(unittest.TestCase):
    def setUp(self):
        """Richtet Testdaten ein, die in mehreren Tests verwendet werden."""
        self.buerger = Buerger(
            buergerid=1,
            vorname="Max",
            nachname="Mustermann",
            geburtstag="1990-01-15",
            adresse="Musterstraße 1",
            plz="12345",
            email="max.mustermann@example.com",
            passwort="geheim",
            rolle="Nutzer",
            authentifizierungsstatus="aktiv"
        )

    def test_voller_name(self):
        """Testet die Methode `voller_name`."""
        self.assertEqual(self.buerger.voller_name(), "Max Mustermann")

    def test_ist_authentifiziert(self):
        """Testet die Methode `ist_authentifiziert`."""
        self.assertTrue(self.buerger.ist_authentifiziert())
        self.buerger.authentifizierungsstatus = "inaktiv"
        self.assertFalse(self.buerger.ist_authentifiziert())

    def test_berechne_alter(self):
        """Testet die Methode `berechne_alter`."""
        heute = datetime.now()
        erwartetes_alter = heute.year - 1990
        if (heute.month, heute.day) < (1, 15):  # Falls der Geburtstag in diesem Jahr noch nicht war.
            erwartetes_alter -= 1
        self.assertEqual(self.buerger.berechne_alter(), erwartetes_alter)

    def test_geburtstag_format_invalid(self):
        """Testet, ob ein Fehler bei ungültigem Datumsformat ausgelöst wird."""
        with self.assertRaises(ValueError):
            Buerger(
                buergerid=2,
                vorname="Anna",
                nachname="Beispiel",
                geburtstag="15-01-1990",  # Falsches Datumsformat
                adresse="Beispielstraße 2",
                plz="54321",
                email="anna.beispiel@example.com",
                passwort="geheim",
                rolle="Admin",
                authentifizierungsstatus="aktiv"
            )

    def test_plz_length(self):
        """Testet die Länge der Postleitzahl (Beispiel für Datenvalidierung)."""
        self.assertEqual(len(self.buerger.plz), 5)


if __name__ == "__main__":
    unittest.main()
