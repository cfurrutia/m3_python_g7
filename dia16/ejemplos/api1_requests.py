import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {}#datos a enviar
headers = {}#formato o tipo de dato

#response = requests.request("GET", url, headers=headers, data=payload)
response = requests.get(url)

print("")
print(response)#<Response [200]>

if response.status_code == 200:#200 OK
    #print(response.text) #convierte la respuesta en un string
    print(response.json())#convierte la respuesta en un JSON
    respuesta = response.json()
    print("")
    print(respuesta["title"])
    print("")
    for clave, valor in respuesta.items():
        print(f"clave {clave} - valor {valor}")
else:
    print("Error en la solicitud",response.status_code)