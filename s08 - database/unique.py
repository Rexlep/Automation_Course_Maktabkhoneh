import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                score INTEGER
            )
""")

try:
    cursor.execute("INSERT INTO members (username, score) VALUES (?, ?)",("Amir", "180"))
    conn.commit()

except sqlite3.IntegrityError:
    print("This username already taken")

conn.close()