import unittest
from main import Bürger, Stimme, Abstimmung
from datetime import datetime, timedelta

# Hier wird angenommen, dass die Klassen Bürger, Stimme und Abstimmung bereits importiert sind.


class TestBürger(unittest.TestCase):
    def test_ist_stimmberechtigt_true(self):
        bürger = Bürger(bürger_id="B1", name="Max Mustermann", email="max@example.com", password="1234",
                        rolle="buerger", authentifizierungsstatus=True, stimmberechtigung=True)
        self.assertTrue(bürger.ist_stimmberechtigt(), "Bürger sollte stimmberechtigt sein")

    def test_ist_stimmberechtigt_false_auth_status(self):
        bürger = Bürger(bürger_id="B2", name="Erika Mustermann", email="erika@example.com", password="1234",
                        rolle="buerger", authentifizierungsstatus=False, stimmberechtigung=True)
        self.assertFalse(bürger.ist_stimmberechtigt(), "Bürger sollte nicht stimmberechtigt sein, da Authentifizierungsstatus False ist")

    def test_ist_stimmberechtigt_false_stimmberechtigung(self):
        bürger = Bürger(bürger_id="B3", name="Hans Muster", email="hans@example.com", password="1234",
                        rolle="buerger", authentifizierungsstatus=True, stimmberechtigung=False)
        self.assertFalse(bürger.ist_stimmberechtigt(), "Bürger sollte nicht stimmberechtigt sein, da Stimmberechtigung False ist")


class TestStimme(unittest.TestCase):
    def test_stimme_creation(self):
        stimme = Stimme(bürger_id="B1", abstimmungs_id="A1", wahloption="Kandidat A")
        self.assertEqual(stimme.bürger_id, "B1", "Bürger-ID sollte korrekt gesetzt sein")
        self.assertEqual(stimme.abstimmungs_id, "A1", "Abstimmungs-ID sollte korrekt gesetzt sein")
        self.assertEqual(stimme.wahloption, "Kandidat A", "Wahloption sollte korrekt gesetzt sein")


class TestAbstimmung(unittest.TestCase):
    def setUp(self):
        self.abstimmung = Abstimmung(
            abstimmungs_id="A1",
            titel="Wahl 2024",
            beschreibung="Wählen Sie Ihren bevorzugten Kandidaten.",
            frist=datetime.now() + timedelta(days=1),  # Setzt die Frist auf morgen
            abstimmungsstatus=True
        )

    def test_add_option(self):
        self.abstimmung.add_option("Kandidat A")
        self.assertIn("Kandidat A", self.abstimmung.verfügbare_optionen, "Option sollte zur Abstimmung hinzugefügt worden sein")

    def test_ist_aktiv_true(self):
        self.assertTrue(self.abstimmung.ist_aktiv(), "Abstimmung sollte aktiv sein, wenn die Frist in der Zukunft liegt und abstimmungsstatus True ist")

    def test_ist_aktiv_false_abgelaufene_frist(self):
        self.abstimmung.frist = datetime.now() - timedelta(days=1)  # Frist auf gestern setzen
        self.assertFalse(self.abstimmung.ist_aktiv(), "Abstimmung sollte inaktiv sein, wenn die Frist abgelaufen ist")

    def test_ist_aktiv_false_abstimmungsstatus(self):
        self.abstimmung.abstimmungsstatus = False
        self.assertFalse(self.abstimmung.ist_aktiv(), "Abstimmung sollte inaktiv sein, wenn abstimmungsstatus False ist")


if __name__ == '__main__':
    unittest.main()
