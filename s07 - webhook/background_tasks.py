import threading
import time
from flask import Flask, request

app = Flask(__name__)


def heavy_tasks(data):
    print("starting tasks")
    time.sleep(2)
    print(f"Task finished for {data.get("user")}")


@app.route('/start-task', methods=['POST'])
def start_task():
    data = request.json
    print(f"{data.get("ln")}")
    thread = threading.Thread(target=heavy_tasks, args=(data,))
    thread.start()

    return {"status": "Task started in background thread"}


if __name__ == '__main__':
    app.run(debug=True)