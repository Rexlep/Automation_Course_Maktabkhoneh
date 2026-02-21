import sqlite3


def create_database():
    conn = sqlite3.connect("market_watcher.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREAMENT,
            title TEXT,
            price REAL,
            availability TEXT,
            sentiment TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Database and Table created successfully!")


if __name__ == "__main__":
    create_database()