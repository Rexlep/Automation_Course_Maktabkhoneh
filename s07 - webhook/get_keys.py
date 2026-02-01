from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    if data:
        print(f"The data value {data.get('password')}")
        return 'OK', 200
    else:
        return 'No data received', 400


if __name__ == '__main__':
    app.run(debug=True)