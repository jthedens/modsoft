import sqlite3

def findCitizens(citizens_mail, citizens_password):
    # Zugriff auf die Datenbank
    conn = sqlite3.connect("../../../../citizens.db")
    # Cursor erstellen
    cursor = conn.cursor()

    res = cursor.execute("SELECT CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED FROM CITIZENS WHERE EMAIL = ? AND PASSWORD = ?",(citizens_mail, citizens_password))
    CITIZENSID, FIRSTNAME, LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED = res.fetchone()

    # Commit your changes in the database
    conn.commit()
    # Closing the connection
    conn.close()

    return CITIZENSID, FIRSTNAME + " " + LASTNAME, EMAIL, PASSWORD, ROLL, AUTHENTICATIONSTATUS, CHOICEALLOWED
