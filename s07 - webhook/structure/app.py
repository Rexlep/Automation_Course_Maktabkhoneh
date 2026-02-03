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


if __name__ == "__main__":
    app.run(debug=True)