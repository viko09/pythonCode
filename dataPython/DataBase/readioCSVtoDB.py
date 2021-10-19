import sqlite3
import csv
import io

conex = sqlite3.connect("ejemplo.db")
cursor = conex.cursor()

file = io.open('data.txt', encoding='latin-1')
# file = open("data.txt")

rows = csv.reader(file)

cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", rows)

cursor.execute("SELECT * FROM students")
# This is for reading
print(cursor.fetchall())

# Saves our changes
conex.commit()
# Close our connection
conex.close()
