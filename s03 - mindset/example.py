import os
import shutil
from datetime import datetime

BASE = "Downloads"

def move(file, folder):
    os.makedirs(folder, exist_ok=True)
    shutil.move(file, folder)


for file in os.listdir(BASE):
    path = os.path.join(BASE, file)

    if not os.path.isfile(path):
        continue

    size = os.path.getsize(path)
    age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(path))

    name = file.lower()

    if file.endswith(".pdf"):
        move(file, "PDF files")

    elif file.endswith(".docx"):
        move(file, "Word files")