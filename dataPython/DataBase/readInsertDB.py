import sqlite3

cnx = sqlite3.connect("ejemplo.db")
cursor = cnx.cursor()

users = [
    ('new1.mail@buap.mx', 'Licenciatura1', 'Name1', 201),
    ('new2.mail@buap.mx', 'Licenciatura2', 'Name2', 202),
    ('new3.mail@buap.mx', 'Licenciatura3', 'Name3', 203),
    ('new4.mail@buap.mx', 'Licenciatura1', 'Nombre4', 201)
]

cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", users)
cnx.commit()

cursor.execute("SELECT * FROM students")
users = cursor.fetchall()

# printing users
for u in users:
    print(u)

cnx.close()
