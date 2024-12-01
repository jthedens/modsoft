# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('stimmen.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
citizensTabel = """CREATE TABLE STIMME(CITIZENSID CHAR(255), ABSTIMMUNGSID CHAR(255), STIMME CHAR(255)) ;"""
cursor.execute(citizensTabel)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()