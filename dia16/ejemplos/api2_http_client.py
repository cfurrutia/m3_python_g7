import http.client

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
payload = ''
headers = {}
conn.request("GET", "/posts", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))