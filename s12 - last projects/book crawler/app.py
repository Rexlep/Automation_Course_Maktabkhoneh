from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)


def get_db_records():
    conn = sqlite3.connect("market_watcher.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    conn.close()
    return data


@app.route("/")
def dashboard():
    rows = get_db_records()

    html_layout = """
    <html>
        <head><title>Market watcher</title></head>
        <body>
            <h1>Bok market Intelligence Dashboard</h1>
            <table border="1" cellpadding="10">
                <tr style="background-color: #f2f2f2;">
                    <th>ID</th>
                    <th>Book Title</th>
                    <th>Price (£)</th>
                    <th>Availability</th>
                    <th>AI Sentiment</th>
                </tr>
                
                {% for  row in data %}
                    <tr style="background-color: #f2f2f2;">
                        <th>{{row[0]}}</th>
                        <th>{{row[1]}}</th>
                        <th>{{row[2]}}</th>
                        <th>{{row[3]}}</th>
                        <th>{{row[4]}}</th>  
                    </tr>  
                {% endfor %}  
            </table>
        </body>
    </html>
    """

    return render_template_string(html_layout, data=rows)


if __name__ == "__main__":
    app.run(debug=True)