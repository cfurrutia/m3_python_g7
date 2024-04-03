import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/"

payload = json.dumps({
    "userId": 1,
    "title": "titulo de ejemplo",
    "body": "esto es un ejemplo del body"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
