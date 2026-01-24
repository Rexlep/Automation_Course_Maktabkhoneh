import requests

headers = {'user-agent': 'agent/1.0.0'}

# response = requests.get("https://maktabkhooneh.org/", headers=headers)
# print(response.text)
# print(response.status_code)
# print(response.headers)
# print(response.url)

response = requests.post('https://www.google.com')

print(response.text)

