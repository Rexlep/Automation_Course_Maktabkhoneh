from flask import Flask, request

warehouse = {"Laptop": 10, "Iphone": 5, "Ps5": 21}

app = Flask(__name__)


@app.route("/")
def index():
    html = "<h1>Warehouse items</h1>"
    html += "<table border=1><tr><th>Item</th><th>Quantity</th></tr>"

    for item, qyn in warehouse.items():
        html += f"<tr><td>{item}</td><td>{qyn}</td></tr>"

    html += "</table>"
    html += "<p>Refresh the page to see updates</p>"
    return html


@app.route("/update", methods=["POST"])
def update():
    data = request.json
    item = data.get('item')
    qyn = data.get('qyn')

    if item and qyn:
        warehouse[item] = qyn
        return {"message": "Inventory updated"}, 200

    return {"error": "Inventory not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)