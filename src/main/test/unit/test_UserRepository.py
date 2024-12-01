import unittest
from unittest.mock import patch, MagicMock
from src.main.python.evoting.infrastructure.repositories.UserRepository import findCitizens
# Die zu testende Funktion importieren
# from your_module import findCitizens  # Passe den Modulpfad an

class TestFindCitizens(unittest.TestCase):

    @patch('sqlite3.connect')  # Mocking der Datenbankverbindung
    def test_find_citizens(self, mock_connect):
        # Mock-Setup
        mock_conn = MagicMock()  # Mock für die Verbindung
        mock_cursor = MagicMock()  # Mock für den Cursor

        # Die Rückgabe der `connect`-Funktion mocken
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Ergebnis der Datenbankabfrage mocken
        mock_cursor.execute.return_value.fetchone.return_value = (
            1, "Max", "Mustermann", "max@example.com", "password123", "User", "Authenticated", "Yes"
        )

        # Funktionsaufruf
        result = findCitizens("max@example.com", "password123")

        # Assertions
        self.assertEqual(result, (
            1,
            "Max Mustermann",
            "max@example.com",
            "password123",
            "User",
            "Authenticated",
            "Yes"
        ))
        mock_cursor.execute.assert_called_once_with(
            "SELECT CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED FROM CITIZENS WHERE EMAIL = ? AND PASSWORD = ?",
            ("max@example.com", "password123")
        )
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
