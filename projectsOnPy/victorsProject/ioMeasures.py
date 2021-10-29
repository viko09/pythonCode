import sqlite3
# This code can input and read data from our database

# Define the connection of our data base
cnx = sqlite3.connect("dataHeart.db")
# Making the cursor
cursor = cnx.cursor()

user = [
    ('24', '196', 10)
]

cursor.executemany("INSERT INTO measures VALUES (?, ?, ?)", user)
cnx.commit()

cursor.execute("SELECT * FROM measures ")
user = cursor.fetchall()

# printing users
for u in user:
    print(u)

# We take one data from our db
user = cursor.fetchone()
cnx.close()
