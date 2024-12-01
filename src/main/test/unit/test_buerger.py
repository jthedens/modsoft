import unittest
from src.main.python.evoting.domain.entities.Buerger import Citizens


class TestCitizens(unittest.TestCase):
    def test_citizens_initialization(self):
        # Testdaten
        citizens_id = 1
        name = "Max Mustermann"
        email = "max.mustermann@example.com"
        password = "securepassword"
        roll = "User"
        authentifizierungsstatus = "Authenticated"
        stimmberechtigung = "Yes"

        # Objekt erstellen
        citizen = Citizens(
            citizens_id,
            name,
            email,
            password,
            roll,
            authentifizierungsstatus,
            stimmberechtigung
        )

        # Assertions: Überprüfung, ob die Attribute korrekt zugewiesen wurden
        self.assertEqual(citizen.citizens_id, citizens_id)
        self.assertEqual(citizen.name, name)
        self.assertEqual(citizen.email, email)
        self.assertEqual(citizen.password, password)
        self.assertEqual(citizen.roll, roll)
        self.assertEqual(citizen.authentifizierungsstatus, authentifizierungsstatus)
        self.assertEqual(citizen.stimmberechtigung, stimmberechtigung)


if __name__ == '__main__':
    unittest.main()
