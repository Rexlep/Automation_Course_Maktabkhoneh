import sqlite3

connection = sqlite3.connect("warehouse.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM inventory WHERE quantity >= 130")
result = cursor.fetchall()

print(result)