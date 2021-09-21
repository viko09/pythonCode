import sqlite3

# Define the connection of our data base
cnx = sqlite3.connect("ejemplo.db")

# Making the cursor
cursor = cnx.cursor()

# Creating a table called students
cursor.execute("CREATE TABLE students (email VARCHAR(100), bachelor VARCHAR(100), name VARCHAR (100), classroom "
               "INTEGER)")

cnx.close()
