from flask import Flask, request
import sqlite3

app = Flask(__name__)


def db_query(query, params=()):
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()


@app.route("/manage", methods=["POST"])
def manage():
    data = request.json
    action = data.get("action")
    name = data.get("name")

    if action == "update":
        new_qty = data.get("new_qty")
        db_query("UPDATE inventory SET quantity = ? WHERE item_name = ?", (new_qty, name))
        return {"msg": f"updated {name} with new quantity {new_qty}"}, 200

    elif action == "delete":
        db_query("DELETE FROM inventory WHERE item_name = ?", (name,))
        return {"msg": f"deleted {name}"}, 200

    return {"error", "Invalid action"}, 404


if __name__ == "__main__":
    app.run(debug=True)
