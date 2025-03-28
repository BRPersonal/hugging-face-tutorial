import requests

url = "http://127.0.0.1:8000/generate"
data = {"prompt": "Once upon a time"}
response = requests.post(url, json=data)

# Print the response
print(response.json())