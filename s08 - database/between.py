import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('select * FROM members WHERE score BETWEEN 50 AND 60')
result = cursor.fetchall()

print(result)
conn.close()