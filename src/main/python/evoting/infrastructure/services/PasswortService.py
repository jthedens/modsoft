import bcrypt

def hashPasswort(passwort):
    """
    Hashes ein Passwort sicher mit einem Salt.

    Args:
        passwort (str): Das Passwort, das gehasht werden soll.

    Returns:
        str: Das gehashte Passwort als String.

    Raises:
        Exception: Wenn beim Hashing ein Fehler auftritt.
    """
    if not passwort:  # Überprüft, ob das Passwort leer oder None ist
        raise ValueError("Das Passwort darf nicht leer sein.")  # Angepasste Exception

    try:
        salt = bcrypt.gensalt()
        hashed_passwort = bcrypt.hashpw(passwort.encode('utf-8'), salt)
        return hashed_passwort.decode('utf-8')  # Als String speichern
    except Exception as e:
        raise Exception(f"Fehler beim Hashen des Passworts: {e}")
