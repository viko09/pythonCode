import sqlite3

# Define the connection of our data base
cnx = sqlite3.connect("dataHeart.db")
# Making the cursor
cursor = cnx.cursor()
# Table with measures
cursor.execute("CREATE TABLE measures (day VARCHAR(100), month VARCHAR(100), measure ""FLOAT)")

cnx.close()
