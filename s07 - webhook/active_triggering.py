import os
import webbrowser
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute", methods=['POST'])
def execute_command():
    data = request.json
    action = data.get('action')

    if action == "open_browser":
        url = data.get('url', "https://google.com")
        webbrowser.open(url)

        return {"message": f"Opening {url}"}, 200

    elif action == "calc":
        os.system("calc")
        return {"message": f"Opening {action}"}, 200

    return {"error": f"Unknown action {action}"}, 400


if __name__ == "__main__":
    app.run(debug=True)