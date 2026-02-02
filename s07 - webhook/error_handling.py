from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json

        if not data:
            return {'error': "JSON body is required"}, 400

        item = data['item']
        quantity = int(data['quantity'])

        return {'status': "success", 'received': item}, 200

    except KeyError as e:
        return {'error': f"Missing field {str(e)}"}, 400
    except ValueError:
        return {'error': "Quantity must be a number"}, 400
    except Exception as e:
        return {'error': f'An error occurred {str(e)}'}, 500


if __name__ == '__main__':
    app.run(debug=True)