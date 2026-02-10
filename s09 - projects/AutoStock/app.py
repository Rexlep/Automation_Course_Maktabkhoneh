from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('monitor.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM price_history ORDER BY update_time DESC LIMIT 5""")
    data = cursor.fetchall()
    conn.close()

    return render_template("index.html", history=data)


if __name__ == '__main__':
    app.run(debug=True)