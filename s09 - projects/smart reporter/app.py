from flask import Flask, render_template
import sqlite3
import config

app = Flask(__name__)


@app.route("/")
def index():
    conn = sqlite3.connect(config.DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''SELECT product, price, date FROM sales_history ORDER BY date''')
    rows = cursor.fetchall()

    cursor.execute('''SELECT SUM(price) FROM sales_history''')
    total = cursor.fetchone()[0] or 0
    conn.close()
    return render_template("index.html", sales=rows, total=total)


if __name__ == "__main__":
    app.run(debug=True)