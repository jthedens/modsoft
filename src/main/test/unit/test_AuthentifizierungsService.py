import unittest
from unittest.mock import patch
from src.main.python.evoting.infrastructure.services.AuthentifizierungsService import AuthentifizierungUser

class TestAuthentifizierungUser(unittest.TestCase):

    @patch("builtins.print")  # Mock für print
    @patch("builtins.input", return_value="Y")  # Mock für Benutzereingabe (User gibt "Y" ein)
    def test_stimmberechtigt_und_authentifiziert(self, mock_input, mock_print):
        # Test: Der User ist berechtigt und authentifiziert
        AuthentifizierungUser(True, True)

        # Überprüfen, ob der entsprechende print-Aufruf gemacht wurde
        mock_print.assert_called_with("User ist berechtigt und authentifiziert")

    @patch("builtins.print")  # Mock für print
    @patch("builtins.input", return_value="N")  # Mock für Benutzereingabe (User gibt "N" ein)
    def test_nicht_authentifiziert_und_stimmberechtigt(self, mock_input, mock_print):
        # Test: Der User ist nicht authentifiziert, aber berechtigt
        AuthentifizierungUser(True, False)

        # Überprüfen, ob der Benutzer gefragt wird, ob er sich authentifizieren möchte
        mock_print.assert_any_call("User ist nicht authentifiziert")
        mock_print.assert_any_call("Authentifizierung abgelehnt")

    @patch("builtins.print")  # Mock für print
    @patch("builtins.input", return_value="N")  # Mock für Benutzereingabe (User gibt "N" ein)
    def test_nicht_authentifiziert_und_nicht_stimmberechtigt(self, mock_input, mock_print):
        # Test: Der User ist weder berechtigt noch authentifiziert
        AuthentifizierungUser(False, False)

        # Überprüfen, dass der Benutzer nicht authentifiziert wird
        mock_print.assert_any_call("User ist nicht berechtigt")

    @patch("builtins.print")  # Mock für print
    @patch("builtins.input", return_value="Y")  # Mock für Benutzereingabe (User gibt "Y" ein)
    def test_nicht_stimmberechtigt_aber_authentifiziert(self, mock_input, mock_print):
        # Test: Der User ist nicht stimmberechtigt, aber authentifiziert
        AuthentifizierungUser(False, True)

        # Überprüfen, dass der Benutzer nicht stimmberechtigt ist
        mock_print.assert_any_call("User ist nicht stimmberechtigt")

if __name__ == "__main__":
    unittest.main()
