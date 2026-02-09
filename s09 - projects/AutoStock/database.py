import sqlite3


def init_db():
    conn = sqlite3.connect('monitor.db')
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                price_value TEXT,
                update_time DATETIME DEFAULT CURRENT_TIMESTAMP)            
    """)

    conn.commit()
    conn.close()
    print('Database initialized.')


if __name__ == '__main__':
    init_db()