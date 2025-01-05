from src.main.python.evoting.domain.entities.Stimme import Stimme
from src.main.python.evoting.infrastructure.services.AbstimmungsService import stimmeErfassen


def stimme_abgeben(buergerid: int, abstimmungid: int, entscheidung: str) -> None:
    """
    Erfasst die Stimme eines Bürgers für eine Abstimmung.

    Args:
        buerger_id (int): Die ID des Bürgers, der abstimmt.
        abstimmung_id (int): Die ID der Abstimmung.
        entscheidung (str): Die Entscheidung des Bürgers.

    Raises:
        ValueError: Wenn einer der Eingabeparameter ungültig ist.
    """
    # Eingabevalidierung
    if not isinstance(buergerid, int) or buergerid <= 0:
        raise ValueError("Die Bürger-ID muss eine positive ganze Zahl sein.")
    if not isinstance(abstimmungid, int) or abstimmungid <= 0:
        raise ValueError("Die Abstimmungs-ID muss eine positive ganze Zahl sein.")
    if not isinstance(entscheidung, str) or not entscheidung.strip():
        raise ValueError("Die Entscheidung muss ein nicht-leerer String sein.")

    # Stimme erstellen und erfassen
    stimme = Stimme(buergerid, abstimmungid, entscheidung)
    stimmeErfassen(stimme.buergerid, stimme.abstimmungid, stimme.entscheidung)
