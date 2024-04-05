import requests
import json

def request_aveschile(url):
    """Obtiene datos de aves de la API especificada mediante una solictud get.

    Returns:
    diccionario : response que contiene toda la informacion de la aves
    """
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error:  {response.status_code}")


if __name__ == "__main__":
    aves_data = request_aveschile('https://aves.ninjas.cl/api/birds')
    print(aves_data)  
    
    
    
    