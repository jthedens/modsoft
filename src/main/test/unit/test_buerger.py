import unittest
from Buerger import Citizens, Stimme

class TestCitizens(unittest.TestCase):
    def setUp(self):
        self.citizen = Citizens(
            citizens_id="C1",
            name="Max Mustermann",
            email="max@example.com",
            password="password123",
            rolle="Bürger",
            authentifizierungsstatus=True,
            stimmberechtigung=True
        )
