import requests, json

def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ == "__main__":
    url = "https://pokeapi.co/api/v2/pokemon/1"
    respuesta = request_get(url)
    
    print(respuesta)