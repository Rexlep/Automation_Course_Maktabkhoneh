from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)


@app.route("/")
def dashboard():
    conn = sqlite3.connect("crm_system.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets ORDER BY id DESC")

    all_tickets = cursor.fetchall()
    conn.close()

    html = """
    <h1>Smart ticket dashboard</h1>
        <table border="1">
            <tr><th>Sender</th><th>Subject</th><th>Content</th><ht>Sentiment status</th></tr>
            {% for  t in tickets %}
            <tr>
                <td>{{t[1]}}</td>
                <td>{{t[2]}}</td>
                <td>{{t[3]}}</td>
                <td>{{t[4]}}</td>
            </tr>
            
            {% endfor %}
        </table>
    """
    return render_template_string(html, tickets=all_tickets)


if __name__ == "__main__":
    app.run(debug=True)