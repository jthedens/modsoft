import unittest  # Bibliothek für Unit-Tests
from src.main.python.evoting.infrastructure.services.PasswortService import hashPasswort
import bcrypt  # Für die Überprüfung des gehashten Passworts


class TestPasswordHashing(unittest.TestCase):
    def test_hashPasswort_returns_hashed_password(self):
        """
        Testet, ob die Funktion ein gehashtes Passwort zurückgibt, das korrekt überprüfbar ist.
        """
        # Eingabe: Originales Passwort
        original_password = "secure_password_123"

        # Rufe die hashPasswort-Funktion auf
        hashed_password = hashPasswort(original_password)

        # Überprüfen, ob der zurückgegebene Hash nicht gleich dem Originalpasswort ist
        self.assertNotEqual(original_password, hashed_password,
                            "Das gehashte Passwort sollte sich vom Original unterscheiden.")

        # Überprüfen, ob das gehashte Passwort korrekt mit bcrypt überprüfbar ist
        self.assertTrue(
            bcrypt.checkpw(original_password.encode('utf-8'), hashed_password.encode('utf-8')),
            "Das gehashte Passwort konnte nicht erfolgreich verifiziert werden."
        )

    def test_hashPasswort_raises_exception_for_empty_password(self):
        """
        Testet, ob die Funktion eine Exception auslöst, wenn ein leeres Passwort übergeben wird.
        """
        with self.assertRaises(ValueError) as context:  # Erwartet jetzt eine ValueError
            hashPasswort("")

        self.assertIn("Das Passwort darf nicht leer sein", str(context.exception),
                      "Die Fehlermeldung sollte auf ein leeres Passwort hinweisen.")


# Führt die Tests aus, wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    unittest.main()
