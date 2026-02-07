from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/add-item', methods=['POST'])
def webhook_to_db():
    data = request.json
    name = data.get("name")
    qty = data.get("qty")

    conn = sqlite3.connect('warehouse.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", (name, qty))
    conn.commit()
    conn.close()

    return {"message": f"saved {name} with this quantity {qty}"}


if __name__ == '__main__':
    app.run(debug=True)