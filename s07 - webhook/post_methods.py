import requests

requests.post('http://127.0.0.1:5000/receiver', json={'msg': 'Hello user'})
