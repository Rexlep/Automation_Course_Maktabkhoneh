import sqlite3

conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO inventory(item_name, quantity) VALUES(?, ?)", ("Laptop", 49))

conn.commit()
conn.close()