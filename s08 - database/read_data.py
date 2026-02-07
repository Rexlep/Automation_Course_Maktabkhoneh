import sqlite3


def get_data():
    conn = sqlite3.connect('warehouse.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()

    if rows[0][1] == 'ablet':
        print("Tablet")

    for row in rows:
        print(f"Id: {row[0]}, Name: {row[1]}, Quantity: {row[2]}")

    conn.close()

get_data()