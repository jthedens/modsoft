from src.main.python.evoting.domain.entities.Buerger import Citizens

def AuthentifizierungUser(stimmberechtigung, authentifizierungsstatus):
    def ist_stimmberechtigt() -> bool:
        return stimmberechtigung and authentifizierungsstatus

    # Hauptlogik
    if ist_stimmberechtigt():
        print("User ist berechtigt und authentifiziert")
    elif not stimmberechtigung and authentifizierungsstatus:
        print("User ist nicht authentifiziert")
        authentifizierungsStatusChange = input("Authentifizieren? (Y/N): ").strip().upper()

        if authentifizierungsStatusChange == "Y":
            authentifizierungsstatus = True  # Variable aktualisieren
            if ist_stimmberechtigt():
                print("User ist nun berechtigt und authentifiziert")
        else:
            print("Authentifizierung abgelehnt")
    else:
        print("User ist nicht berechtigt")