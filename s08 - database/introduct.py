import sqlite3

connection = sqlite3.connect('warehouse.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        quantity INTEGER DEFAULT 0
    )""")

connection.commit()
connection.close()