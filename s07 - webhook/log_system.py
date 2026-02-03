from flask import Flask, request

app = Flask(__name__)


@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    event = data.get('event')
    user = data.get('user')
    with open("activity.txt", "a+") as f:
        f.write(f"User : {user} Event : {event} \n")

    return {"status": "success", "event": event, "user": user, "message": "Log Created Successfully"}


if __name__ == '__main__':
    app.run(debug=True)