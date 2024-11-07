# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('citizens.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
citizensTabel = """CREATE TABLE CITIZENS(CITIZENSID VARCHAR(255), FIRSTNAME VARCHAR(255), LASTNAME VARCHAR(255), 
DATEOFBIRTH VARCHAR(255), EMAIL VARCHAR(255), PASSWORD VARCHAR(255), ROLL VARCHAR(255), AUTHENTICATIONSTATUS, CHOICEALLOWED ) ;"""
cursor.execute(citizensTabel)

# Queries to INSERT records.
cursor.execute('''INSERT INTO CITIZENS VALUES ('100001', 'Max', 'Müller', '28.06.1965', 'max.m@mail.de', '1234', 'Bürger', '0', '0')''')
cursor.execute('''INSERT INTO CITIZENS VALUES ('100002', 'Petra', 'Meyer', '01.02.1991', 'petra.m@mail.de', '1234', 'Bürger','0', '0')''')
cursor.execute('''INSERT INTO CITIZENS VALUES ('100003', 'Anna', 'Schmidt', '30.12.2007', 'anna.s@mail.de', '1234','Bürger', '0', '0')''')

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()