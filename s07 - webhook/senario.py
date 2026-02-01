from flask import Flask, request

app = Flask(__name__)


@app.route('/secure-webhook', methods=['POST'])
def secure_handler():
    data = request.json

    if data.get('api_key') == "token-1234":
        user_msg = data.get('msg')
        print(f"Message {user_msg}")
        return {'status': 'authorized', 'msg': 'done'}, 200
    else:
        return {'status': 'unauthorized', 'msg': 'Access denied'}, 401


if __name__ == '__main__':
    app.run(debug=True)