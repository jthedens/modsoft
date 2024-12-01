def AuthentifizierungUser(stimmberechtigung, authentifizierungsstatus):
    def ist_stimmberechtigt() -> bool:
        return stimmberechtigung and authentifizierungsstatus

    # Hauptlogik
    if ist_stimmberechtigt():
        print("User ist berechtigt und authentifiziert")
    elif not authentifizierungsstatus:
        print("User ist nicht authentifiziert")  # Falls der Benutzer nicht authentifiziert ist
        authentifizierungsStatusChange = input("Authentifizieren? (Y/N): ").strip().upper()

        if authentifizierungsStatusChange == "Y":
            authentifizierungsstatus = True  # Variable aktualisieren
            if ist_stimmberechtigt():
                print("User ist nun berechtigt und authentifiziert")
        else:
            print("Authentifizierung abgelehnt")
    elif not stimmberechtigung:
        print("User ist nicht stimmberechtigt")  # Falls der Benutzer nicht stimmberechtigt ist
    else:
        print("User ist nicht berechtigt")  # Falls der Benutzer nicht stimmberechtigt und nicht authentifiziert ist
