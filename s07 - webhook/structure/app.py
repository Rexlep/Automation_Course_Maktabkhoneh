import os

from flask import Flask, render_template, request


services = {
    "Dashboard": "Online",
    "Main-server": 'Online',
    "selenium-server": "Ofline"
}


app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template('index.html', services=services)


@app.route("/update-status", methods=['POST'])
def update_status():
    data = request.json
    service_name = data.get('service_name')
    new_status = data.get('status')

    if service_name in services:
        services[service_name] = new_status
        return {'status': "updated"}, 200

    return {"error": "service not found"}, 404


@app.route("/run-script", methods=['POST'])
def update_service():
    print("User clicked on button")

    os.system("notepad.exe")

    return '<h1>Success script is running now</h1><a href="/">Back to Home</a>'


if __name__ == "__main__":
    app.run(debug=True)