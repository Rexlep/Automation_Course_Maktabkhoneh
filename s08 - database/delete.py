import sqlite3


def delete_item(name):
    conn = sqlite3.connect('warehouse.db')
    cursor = conn.cursor()

    query = "DELETE FROM inventory WHERE item_name = ?"

    cursor.execute(query, (name,))

    conn.commit()
    conn.close()
    print(f"Item {name} deleted")


delete_item("PS5")