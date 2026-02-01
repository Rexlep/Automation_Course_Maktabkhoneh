from flask import Flask, request

app = Flask(__name__)


@app.route('/receiver', methods=['POST'])
def webhook_handler():
    data = request.json
    if data:
        print(f"I received this data: {data}")
        return 'OK the data has been received', 200
    else:
        print(f"I did not receive any data")
        return 'NOT OK no data received', 400


if __name__ == '__main__':
    app.run(debug=True)