import unittest
from unittest.mock import patch
from src.main.python.evoting.domain.entities.Abstimmung import Abstimmung
from src.main.python.evoting.infrastructure.repositories.AbstimmungRepository import abstimmungErstellen
from src.main.python.evoting.infrastructure.services.abstimmung_service import abstimmung_erstellen

class TestAbstimmungErstellen(unittest.TestCase):
    @patch("src.main.python.evoting.infrastructure.repositories.AbstimmungRepository.abstimmungErstellen")
    def test_abstimmung_erstellen_erfolgreich(self, mock_abstimmungErstellen):
        """
        Testet, ob eine Abstimmung erfolgreich erstellt wird.
        """
        mock_abstimmungErstellen.return_value = None  # Simuliere Erfolg beim Speichern

        # Eingabewerte
        abstimmungid = 1
        titel = "Test Abstimmung"
        beschreibung = "Dies ist eine Testabstimmung."
        frist = "2025-12-31"
        altersgrenze = 18
        status = "offen"

        # Funktion aufrufen
        try:
            abstimmung_erstellen(abstimmungid, titel, beschreibung, frist, altersgrenze, status)
        except Exception:
            self.fail("abstimmung_erstellen hat unerwartet eine Exception geworfen.")

        # Sicherstellen, dass die Repository-Methode aufgerufen wurde
        mock_abstimmungErstellen.assert_called_once_with(
            abstimmungid, titel, beschreibung, frist, altersgrenze, status
        )

    def test_abstimmung_erstellen_eingabefehler(self):
        """
        Testet, ob Eingabefehler korrekt behandelt werden.
        """
        with self.assertRaises(ValueError):
            abstimmung_erstellen(
                abstimmungid=1,
                titel="",
                beschreibung="Beschreibung vorhanden",
                frist="2025-12-31",
                altersgrenze=18,
                status="offen"
            )

        with self.assertRaises(ValueError):
            abstimmung_erstellen(
                abstimmungid=1,
                titel="Test",
                beschreibung="",
                frist="2025-12-31",
                altersgrenze=18,
                status="offen"
            )

        with self.assertRaises(ValueError):
            abstimmung_erstellen(
                abstimmungid=1,
                titel="Test",
                beschreibung="Beschreibung vorhanden",
                frist="2025-12-31",
                altersgrenze=-1,
                status="offen"
            )

        with self.assertRaises(ValueError):
            abstimmung_erstellen(
                abstimmungid=1,
                titel="Test",
                beschreibung="Beschreibung vorhanden",
                frist="2025-12-31",
                altersgrenze=18,
                status="invalid_status"
            )

    @patch("src.main.python.evoting.infrastructure.repositories.AbstimmungRepository.abstimmungErstellen")
    def test_abstimmung_erstellen_unexpected_error(self, mock_abstimmungErstellen):
        """
        Testet, ob unerwartete Fehler korrekt behandelt werden.
        """
        mock_abstimmungErstellen.side_effect = Exception("Datenbankfehler")

        with self.assertRaises(Exception) as context:
            abstimmung_erstellen(
                abstimmungid=1,
                titel="Test",
                beschreibung="Beschreibung vorhanden",
                frist="2025-12-31",
                altersgrenze=18,
                status="offen"
            )

        self.assertIn("Datenbankfehler", str(context.exception))

if __name__ == "__main__":
    unittest.main()
