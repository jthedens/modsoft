from src.main.python.evoting.domain.entities.Abstimmung import Abstimmung
from src.main.python.evoting.infrastructure.repositories.AbstimmungRepository import abstimmungErstellen

def abstimmung_erstellen(
    abstimmungid: int,
    titel: str,
    beschreibung: str,
    frist: str,
    altersgrenze: int,
    status: str
) -> None:
    """
    Erstellt eine neue Abstimmung und speichert sie in der Datenbank.

    Args:
        abstimmungid (int): Die ID der Abstimmung.
        titel (str): Der Titel der Abstimmung.
        beschreibung (str): Eine Beschreibung der Abstimmung.
        frist (str): Die Frist für die Abstimmung (z. B. "YYYY-MM-DD").
        altersgrenze (int): Mindestalter für die Teilnahme.
        status (str): Status der Abstimmung (z. B. "offen", "geschlossen").

    Raises:
        ValueError: Wenn eine der Eingaben ungültig ist.
        Exception: Für unerwartete Fehler.
    """
    try:
        # Überprüfung der Eingabedaten
        if not titel or not beschreibung:
            raise ValueError("Titel und Beschreibung dürfen nicht leer sein.")
        if altersgrenze < 0:
            raise ValueError("Die Altersgrenze darf nicht negativ sein.")
        if status not in {"offen", "geschlossen"}:
            raise ValueError("Status muss 'offen' oder 'geschlossen' sein.")

        # Abstimmung-Objekt erstellen
        abstimmung = Abstimmung(abstimmungid, titel, beschreibung, frist, altersgrenze, status)

        # Abstimmung in die Datenbank speichern
        abstimmungErstellen(
            abstimmung.abstimmungid,
            abstimmung.titel,
            abstimmung.beschreibung,
            abstimmung.frist,
            abstimmung.altersgrenze,
            abstimmung.status
        )

        print(f"Abstimmung mit ID {abstimmungid} wurde erfolgreich erstellt!")

    except ValueError as ve:
        print(f"Eingabefehler: {ve}")
        raise
    except Exception as e:
        print(f"Fehler beim Erstellen der Abstimmung: {e}")
        raise
