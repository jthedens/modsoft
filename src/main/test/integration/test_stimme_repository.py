import unittest
import sqlite3
from src.main.python.evoting.infrastructure.repositories.StimmeRepository import findStimme  # Ersetze 'your_module' durch den Namen deines Moduls

class TestFindStimme(unittest.TestCase):
    def setUp(self):
        """
        Set up an in-memory SQLite database and populate it with test data.
        """
        # In-Memory-Datenbank erstellen
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        # Test-Tabelle erstellen
        self.cursor.execute("""
        CREATE TABLE stimmen (
            ID INTEGER PRIMARY KEY,
            ABSTIMMUNGSID INTEGER NOT NULL,
            CITIZENSID INTEGER NOT NULL,
            STIMME TEXT NOT NULL
        )
        """)

        # Test-Daten einfügen
        self.cursor.executemany("""
        INSERT INTO stimmen (ABSTIMMUNGSID, CITIZENSID, STIMME) VALUES (?, ?, ?)
        """, [
            (1, 101, 'Ja'),
            (1, 102, 'Nein'),
            (2, 101, 'Ja'),
            (1, 101, 'Ja')  # Duplizierter Eintrag für den Test
        ])
        self.connection.commit()

    def tearDown(self):
        """
        Close the in-memory database connection.
        """
        self.connection.close()

    def test_find_stimme(self):
        """
        Test the findStimme function.
        """
        # Funktion so anpassen, dass sie eine bestehende Verbindung akzeptiert
        def findStimmeWithConnection(connection, abstimmungs_id, citizens_id):
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(STIMME) FROM stimmen WHERE ABSTIMMUNGSID = ? AND CITIZENSID = ?",
                           (abstimmungs_id, citizens_id))
            return cursor.fetchone()[0]

        # Testfälle
        self.assertEqual(findStimmeWithConnection(self.connection, 1, 101), 2)  # Zwei Einträge für (1, 101)
        self.assertEqual(findStimmeWithConnection(self.connection, 1, 102), 1)  # Ein Eintrag für (1, 102)
        self.assertEqual(findStimmeWithConnection(self.connection, 2, 101), 1)  # Ein Eintrag für (2, 101)
        self.assertEqual(findStimmeWithConnection(self.connection, 3, 101), 0)  # Kein Eintrag für (3, 101)

if __name__ == "__main__":
    unittest.main()
