import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {}
headers = {}

response = requests.delete(url)

print(response.text)
print(response.status_code)
