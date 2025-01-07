# Importieren des sqlite3-Moduls, um mit SQLite-Datenbanken zu arbeiten
import sqlite3
import bcrypt # Für Passwort-Hashing
import uuid

# Verbindung zur SQLite-Datenbank herstellen (wenn die Datei nicht existiert, wird sie erstellt)
conn = sqlite3.connect('eVoteMain.db')

# Erstellen eines Cursors, um SQL-Befehle auszuführen
cursor = conn.cursor()

###########################
#### Datenbank: Bürger ####
###########################

# Erstellen der Tabelle 'buerger', wenn sie noch nicht existiert
# Die Tabelle enthält grundlegende Informationen über die Bürger, einschließlich einer eindeutigen ID
cursor.execute(
    """CREATE TABLE IF NOT EXISTS buerger (
    buergerid INTEGER NOT NULL,                   -- Eindeutige ID für jeden Bürger
    vorname TEXT NOT NULL,                        -- Vorname des Bürgers
    nachname TEXT NOT NULL,                       -- Nachname des Bürgers
    geburtstag DATE NOT NULL,                     -- Geburtsdatum im Format YYYY-MM-DD
    adresse TEXT NOT NULL,                        -- Adresse des Bürgers
    plz TEXT NOT NULL,                            -- Postleitzahl
    email TEXT NOT NULL UNIQUE,                   -- E-Mail-Adresse (muss eindeutig sein)
    passwort TEXT NOT NULL,                       -- Passwort (normalerweise gehasht)
    rolle TEXT NOT NULL,                          -- Rolle des Bürgers (z.B. "Benutzer", "Admin")
    authentifizierungsstatus INTEGER NOT NULL    -- Authentifizierungsstatus (0 = nicht authentifiziert, 1 = authentifiziert)
);
""")

### Beispiel-Daten in die Tabelle 'buerger' einfügen

# Benutzerdefiniertes Passwort
passwort = "1234"

# Salt erzeugen (bcrypt wird automatisch ein zufälliges Salt hinzufügen)
salt = bcrypt.gensalt()

# Passwort mit Salt hashen
hashed_passwort = bcrypt.hashpw(passwort.encode('utf-8'), salt)

# Gehashtes Passwort ausgeben
# print("Gehashtes Passwort:", hashed_passwort.decode('utf-8'))


cursor.execute("""
INSERT INTO buerger (
    buergerid, vorname, nachname, geburtstag, adresse, plz, email, passwort, rolle, authentifizierungsstatus
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    156418,               # ID des Bürgers
    'Max',                # Vorname
    'Mustermann',         # Nachname
    '1996-07-26',         # Geburtsdatum
    'Musterstraße 12',    # Adresse
    '12345',              # Postleitzahl
    'max@mail.de',        # E-Mail-Adresse
    hashed_passwort,      # Passwort
    'Benutzer',           # Rolle
    1                     # Authentifizierungsstatus (1 = authentifiziert)
))

###########################
## Datenbank: Abstimmung ##
###########################

# Erstellen der Tabelle 'abstimmung', wenn sie noch nicht existiert
# Diese Tabelle enthält Informationen zu Abstimmungen (z.B. Titel, Beschreibung und Frist)
cursor.execute(
    """CREATE TABLE IF NOT EXISTS abstimmung (
    abstimmungid TEXT PRIMARY KEY,  -- UUID statt INTEGER
    titel TEXT NOT NULL,
    beschreibung TEXT NOT NULL,
    frist DATE NOT NULL,
    altersgrenze INTEGER NOT NULL,
    status INTEGER NOT NULL
);

""")

# Beispiel-Daten in die Tabelle 'abstimmung' einfügen
cursor.execute("""
INSERT INTO abstimmung (
    abstimmungid, titel, beschreibung, frist, altersgrenze, status
) VALUES (?, ?, ?, ?, ?, ?)
""", (
    4678,
    'Titel der Abstimmung',                        # Titel der Abstimmung
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Integer convallis, ...',  # Beschreibung
    '2026-02-01',                                  # Frist für die Abstimmung
    18,                                            # Altersgrenze
    'aktiv'                                        # Status (1 = aktiv)
))

cursor.execute("""
INSERT INTO abstimmung (
    abstimmungid, titel, beschreibung, frist, altersgrenze, status
) VALUES (?, ?, ?, ?, ?, ?)
""", (
    9745,
    'Neue Parkanlage',                             # Titel der Abstimmung
    'Soll eine neue Parkanlage im Stadtzentrum gebaut werden?',  # Beschreibung
    '2025-10-28',                                  # Frist für die Abstimmung
    18,                                            # Altersgrenze
    'aktiv'                                        # Status (1 = aktiv)
))

###########################
## Datenbank: Auswertung ##
###########################

# Erstellen der Tabelle 'auswertung', wenn sie noch nicht existiert
# Diese Tabelle speichert die Abstimmungsergebnisse der Bürger
cursor.execute(
    """CREATE TABLE IF NOT EXISTS auswertung (
    buergerid INTEGER NOT NULL,                       -- ID des Bürgers, der abgestimmt hat
    abstimmungid INTEGER NOT NULL,                    -- ID der Abstimmung, auf die der Bürger reagiert hat
    stimme TEXT NOT NULL                              -- Die abgegebene Stimme (z.B. 'A' oder 'B')
);
""")

# Beispiel-Daten in die Tabelle 'auswertung' einfügen
cursor.execute("""
INSERT INTO auswertung (
    buergerid, abstimmungid, stimme
) VALUES (?, ?, ?)
""", (
    12345, 123, "A"  # Bürger 12345 hat bei Abstimmung 123 mit 'A' abgestimmt
))
cursor.execute("""
INSERT INTO auswertung (
    buergerid, abstimmungid, stimme
) VALUES (?, ?, ?)
""", (
    12346, 123, "B"  # Bürger 12346 hat bei Abstimmung 123 mit 'B' abgestimmt
))

# Änderungen in der Datenbank speichern
conn.commit()

# Verbindung zur Datenbank schließen
conn.close()
