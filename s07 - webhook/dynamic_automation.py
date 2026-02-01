from flask import Flask, request

app = Flask(__name__)

warehouse_items = {}


@app.route('/invertory', methods=['POST'])
def manage_invertory():
    data = request.json
    if not data:
        return 'No data provided', 400

    action = data.get('action')
    item = data.get('item')
    quantity = data.get('quantity', 1)

    if action == 'add':
        if item in warehouse_items:
            warehouse_items[item] += quantity
        else:
            warehouse_items[item] = quantity
            print(f"Added {item} with this quentity {quantity}")

    elif action == 'remove':
        if item in warehouse_items:
            del warehouse_items[item]
            print(f"Removed {item}")

        else:
            print(f"Item {item} is not in warehouse items")

    elif action == 'show':
        print(f'Current invertory: {warehouse_items}')
        return {'invertory': warehouse_items}, 200

    else:
        return 'Invalid action', 400
    return "Action completed successfully", 200


if __name__ == '__main__':
    app.run(debug=True)