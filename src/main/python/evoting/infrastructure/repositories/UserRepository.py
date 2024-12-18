import sqlite3

def find_citizens(citizens_mail, citizens_password):
  try:
    # Zugriff auf die Datenbank
    conn = sqlite3.connect("../../../../citizens.db")
    # Cursor erstellen
    cursor = conn.cursor()

    result = cursor.execute("SELECT CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLE, AUTHENTICATIONSTATUS, CHOICEALLOWED FROM CITIZENS WHERE EMAIL = ? AND PASSWORD = ?",(citizens_mail, citizens_password))
    CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED = result.fetchone()

    if result is None:
      raise ValueError("Kein Benutzer gefunden. Ungültige Email oder Passwort.")

    return (
        result[0],  # CITIZENSID
        f"{result[1]} {result[2]}",  # FIRSTNAME + LASTNAME
        result[3],  # EMAIL
        result[4],  # PASSWORD
        result[5],  # ROLE
        result[6],  # AUTHENTICATIONSTATUS
        result[7],  # CHOICEALLOWED
      )

  except sqlite3.Error as e:
    print(f"Datenbankfehler: {e}")
    raise
  finally:
    conn.close()


    # # Commit your changes in the database
    # conn.commit()
    # # Closing the connection
    # conn.close()

    # return CITIZENSID, FIRSTNAME + " " + LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED

def add_citizen_to_database(name, email, password):
    try:
        conn = sqlite3.connect("citizens.db")
        cursor = conn.cursor()

        # Passwort-Hashing hinzufügen (empfohlen)
        hashed_password = password  # Hier könntest du `werkzeug.security` verwenden

        cursor.execute(
            "INSERT INTO CITIZENS (FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (name.split()[0], name.split()[1], email, hashed_password, "user", 0, 1)
        )
        conn.commit()
    except sqlite3.Error as e:
        raise Exception(f"Fehler beim Hinzufügen zur Datenbank: {e}")
    finally:
        conn.close()
