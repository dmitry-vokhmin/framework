import sqlite3

connection = sqlite3.connect('patterns.sqlite')
cursor = connection.cursor()
with open('create_db.sql', 'r') as file:
    text = file.read()
cursor.executescript(text)
cursor.close()
connection.close()
