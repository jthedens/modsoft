import unittest
from unittest.mock import patch
from src.main.python.evoting.domain.entities.Buerger import Buerger
from src.main.python.evoting.infrastructure.services.AuthentifizierungsService import AuthentifizierungUser
from src.main.python.evoting.infrastructure.repositories.UserRepository import findCitizens

class TestMainFlow(unittest.TestCase):

    @patch('src.main.python.evoting.infrastructure.repositories.UserRepository.findCitizens')
    @patch('src.main.python.evoting.infrastructure.services.LoginService.UserLogin')
    @patch('src.main.python.evoting.infrastructure.services.AuthentifizierungsService.AuthentifizierungUser')
    def test_main_flow(self, mock_authentifizierung_user, mock_user_login, mock_find_citizens):
        # Mock für UserLogin
        mock_user_login.return_value = ("user@example.com", "securepassword")

        # Mock für findCitizens
        mock_find_citizens.return_value = (
            "1", "Max Mustermann", "max.mustermann@example.com", "securepassword", "User", "Authenticated", "Yes"
        )

        # Mock für AuthentifizierungUser
        mock_authentifizierung_user.return_value = None  # Angenommen: keine Rückgabe

        # Code-Simulation
        userMail, userPassword = mock_user_login()  # Auf den Mock zugreifen
        dataCitizens = mock_find_citizens(userMail, userPassword)
        citizens = Citizens(dataCitizens[0], dataCitizens[1], dataCitizens[2], dataCitizens[3],
                            dataCitizens[4], dataCitizens[5], dataCitizens[6])
        mock_authentifizierung_user(citizens.stimmberechtigung, citizens.authentifizierungsstatus)

        # Assertions
        mock_user_login.assert_called_once()
        mock_find_citizens.assert_called_once_with("user@example.com", "securepassword")
        mock_authentifizierung_user.assert_called_once_with("Yes", "Authenticated")

        # Überprüfen, ob Citizens-Objekt korrekt erstellt wurde
        self.assertEqual(citizens.citizens_id, "1")
        self.assertEqual(citizens.name, "Max Mustermann")
        self.assertEqual(citizens.email, "max.mustermann@example.com")
        self.assertEqual(citizens.password, "securepassword")
        self.assertEqual(citizens.roll, "User")
        self.assertEqual(citizens.authentifizierungsstatus, "Authenticated")
        self.assertEqual(citizens.stimmberechtigung, "Yes")


if __name__ == '__main__':
    unittest.main()
