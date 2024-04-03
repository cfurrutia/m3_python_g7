import requests


url = "https://jsonplaceholder.typicode.com/posts/"

payload = {
    "userId": 1,
    "title": "titulo de ejemplo",
    "body": "esto es un ejemplo del body"
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload)

print(response.text)

if response.status_code == 201:
    print("Insercion exitosa")
    
else:
    print("Error en la creacion del posts")    