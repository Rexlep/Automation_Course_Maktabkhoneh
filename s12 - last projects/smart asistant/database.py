import sqlite3


def init_db():
    conn = sqlite3.connect("crm_system.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tickets
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender  TEXT,
                        subject TEXT,
                        content TEXT,
                        sentiment TEXT
    """)

    conn.commit()
    conn.close()


def save_ticket(sender, subject, content, sentiment):
    conn = sqlite3.connect("crm_system.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (sender, subject, content, sentiment) VALUES (?, ?, ?, ?)",
                   (sender, subject, content, sentiment))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Data base initialized")