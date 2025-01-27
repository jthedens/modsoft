import unittest
from unittest.mock import patch
from src.main.python.evoting.domain.entities.Stimme import Stimme
from src.main.python.evoting.infrastructure.services.AbstimmungsService import stimmeErfassen
from src.main.python.evoting.infrastructure.services.abstimmung_service import stimme_abgeben


class TestStimmeAbgeben(unittest.TestCase):
    @patch("src.main.python.evoting.infrastructure.services.AbstimmungsService.stimmeErfassen")
    def test_stimme_abgeben_erfolgreich(self, mock_stimmeErfassen):
        """
        Testet, ob die Funktion erfolgreich eine Stimme erfasst.
        """
        mock_stimmeErfassen.return_value = None  # Simuliere Erfolg beim Erfassen

        # Gültige Eingabewerte
        buergerid = 1
        abstimmungid = 100
        entscheidung = "Ja"

        try:
            stimme_abgeben(buergerid, abstimmungid, entscheidung)
        except Exception:
            self.fail("stimme_abgeben hat unerwartet eine Exception geworfen.")

        # Überprüfen, ob stimmeErfassen mit den richtigen Parametern aufgerufen wurde
        mock_stimmeErfassen.assert_called_once_with(buergerid, abstimmungid, entscheidung)

    def test_stimme_abgeben_eingabefehler(self):
        """
        Testet, ob die Funktion bei ungültigen Eingaben Fehler auslöst.
        """
        with self.assertRaises(ValueError):
            stimme_abgeben(-1, 100, "Ja")  # Ungültige Bürger-ID

        with self.assertRaises(ValueError):
            stimme_abgeben(1, -100, "Ja")  # Ungültige Abstimmungs-ID

        with self.assertRaises(ValueError):
            stimme_abgeben(1, 100, "")  # Leere Entscheidung

        with self.assertRaises(ValueError):
            stimme_abgeben(1, 100, None)  # Ungültige Entscheidung (None)

    @patch("src.main.python.evoting.infrastructure.services.AbstimmungsService.stimmeErfassen")
    def test_stimme_abgeben_unexpected_error(self, mock_stimmeErfassen):
        """
        Testet, ob die Funktion korrekt auf unerwartete Fehler reagiert.
        """
        mock_stimmeErfassen.side_effect = Exception("Datenbankfehler")

        with self.assertRaises(Exception) as context:
            stimme_abgeben(1, 100, "Ja")

        self.assertIn("Datenbankfehler", str(context.exception))


if __name__ == "__main__":
    unittest.main()