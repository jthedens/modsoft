import sqlite3

def abgebenStimme(stimmberechtigung, citizensID, abstimmungsID):

    if stimmberechtigung:
        stimme = input("Option 1 oder 2: ")

        # Verbindung zur Datenbank herstellen
        connection = sqlite3.connect("../../../../stimmen.db")
        cursor = connection.cursor()

        # SQL-Befehl zum Einfügen eines Eintrags
        insert_query = '''INSERT INTO users (CITIZENSID, ABSTIMMUNGSID, STIMME) VALUES (?, ?, ?)'''

        # Werte, die eingefügt werden sollen
        values = (abstimmungsID, citizensID, stimme)

        # SQL-Befehl ausführen
        cursor.execute(insert_query, values)

        # Änderungen speichern
        connection.commit()

        # Verbindung schließen
        connection.close()

        print("Eintrag erfolgreich hinzugefügt.")


