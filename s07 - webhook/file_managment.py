import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/files", methods=['POST'])
def create_folder():
    data = request.json
    folder_name = data.get('folder')

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        return {'status': "successfully created the folder", "path": folder_name}, 201
    else:
        return {'status': "Folder already exists"}, 200


if __name__ == "__main__":
    app.run(debug=True)