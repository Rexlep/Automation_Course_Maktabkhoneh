import sqlite3

conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO inventory(item_name, quantity) VALUES(?, ?)", ("iphone", 120))

conn.commit()
conn.close()