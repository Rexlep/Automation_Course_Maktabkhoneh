import sqlite3


def update_items(id, new_name):
    conn = sqlite3.connect('warehouse.db')
    cursor = conn.cursor()
    query = "UPDATE inventory SET item_name = ? WHERE id = ?"

    cursor.execute(query,(new_name, id))

    conn.commit()
    conn.close()
    print(f"Item {id} has been updated with this name {new_name}")


update_items(1, "PS5")