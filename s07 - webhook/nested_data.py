from flask import Flask, request

app = Flask(__name__)


@app.route('/crypto-update', methods=['POST'])
def crypto_handler():
    data = request.json

    for coin in data['prices']:
        symbol = coin['symbol']
        price = coin['value']

        if price > 40000:
            print(f"This coin {symbol} is getting expensive price : {price}")

    return "monitoring is done", 200


if __name__ == '__main__':
    app.run(debug=True)