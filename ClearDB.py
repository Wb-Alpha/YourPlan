import sqlite3

database = sqlite3.connect("YourPlan.db")
conn = database.cursor()

conn.execute('''drop database;''')