from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'


@app.route('/')
def index():
    return redirect(url_for('login_page'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == "POST":
        user = request.form.get('username')
        password = request.form.get('password')

        if user == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to Dashboard</h1><p>Only admins can see this</p>"


if __name__ == '__main__':
    app.run(debug=True)