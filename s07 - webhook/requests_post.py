import requests

url = "http://127.0.0.1:5000/log"

data = {"event": "sending tickets", "user": "Amir"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
