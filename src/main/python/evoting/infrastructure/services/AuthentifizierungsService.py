import logging

# Logger konfigurieren
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# AuthentifizierungUser-Funktion mit Logger
def AuthentifizierungUser(stimmberechtigung, authentifizierungsstatus):
    logger.info("AuthentifizierungUser aufgerufen")
    logger.info(f"Initialer Status - Stimmberechtigung: {stimmberechtigung}, Authentifizierungsstatus: {authentifizierungsstatus}")

    def ist_stimmberechtigt() -> bool:
        return stimmberechtigung and authentifizierungsstatus

    # Hauptlogik
    if ist_stimmberechtigt():
        logger.info("User ist stimmberechtigt und authentifiziert")
        print("User ist berechtigt und authentifiziert")
    elif not authentifizierungsstatus:
        logger.warning("User ist nicht authentifiziert")
        print("User ist nicht authentifiziert")
        authentifizierungsStatusChange = input("Authentifizieren? (Y/N): ").strip().upper()

        if authentifizierungsStatusChange == "Y":
            authentifizierungsstatus = True
            logger.info("Authentifizierungsstatus wurde aktualisiert auf True")
            if ist_stimmberechtigt():
                logger.info("User ist jetzt stimmberechtigt und authentifiziert")
                print("User ist nun berechtigt und authentifiziert")
        else:
            logger.warning("Authentifizierung abgelehnt")
            print("Authentifizierung abgelehnt")
    elif not stimmberechtigung:
        logger.warning("User ist nicht stimmberechtigt")
        print("User ist nicht stimmberechtigt")
    else:
        logger.warning("User ist nicht berechtigt")
        print("User ist nicht berechtigt")
