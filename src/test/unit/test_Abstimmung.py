import unittest
from datetime import datetime, timedelta
from src.main.python.evoting.domain.entities.Abstimmung import Abstimmung

class TestAbstimmung(unittest.TestCase):
    def test_ist_verfuegbar_true(self):
        """
        Testet, ob `ist_verfuegbar` True zurückgibt, wenn die Frist in der Zukunft liegt.
        """
        future_date = datetime.now() + timedelta(days=1)
        abstimmung = Abstimmung(
            abstimmungid=1,
            titel="Test Abstimmung",
            beschreibung="Test Beschreibung",
            frist=future_date,
            altersgrenze=18,
            status="aktiv"
        )
        self.assertTrue(abstimmung.ist_verfuegbar())

    def test_ist_verfuegbar_false(self):
        """
        Testet, ob `ist_verfuegbar` False zurückgibt, wenn die Frist in der Vergangenheit liegt.
        """
        past_date = datetime.now() - timedelta(days=1)
        abstimmung = Abstimmung(
            abstimmungid=2,
            titel="Vergangene Abstimmung",
            beschreibung="Beschreibung",
            frist=past_date,
            altersgrenze=18,
            status="abgeschlossen"
        )
        self.assertFalse(abstimmung.ist_verfuegbar())

    def test_ist_verfuegbar_now(self):
        """
        Testet, ob `ist_verfuegbar` True zurückgibt, wenn die Frist genau jetzt liegt.
        """
        now_date = datetime.now()
        abstimmung = Abstimmung(
            abstimmungid=3,
            titel="Jetzt Abstimmung",
            beschreibung="Beschreibung",
            frist=now_date,
            altersgrenze=18,
            status="aktiv"
        )
        self.assertTrue(abstimmung.ist_verfuegbar())

if __name__ == "__main__":
    unittest.main()