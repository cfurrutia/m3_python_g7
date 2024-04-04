import requests

"""
Obtenga toda la información de los usuarios retornada por la API, guárdela en una 
variable llamada users_data e imprímala en pantalla. 
"""
response = requests.get("https://reqres.in/api/users/")
users_data = response.json()
print(users_data)
"""
Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el 
diccionario de respuesta en una variable llamada created_user e imprímala en 
pantalla 
"""
user_data = {"first_name": "Ignacio","job": "Profesor"}

response = requests.post("https://reqres.in/api/users/", json=user_data)
created_user = response.json()
print(created_user)

"""
Actualice un usuario llamado morpheus para que tenga un campo llamado residence
igual a zion. Guarde el diccionario de respuesta en una variable llamada 
updated_user e imprímala en pantalla.  
"""
user_data = {"name": "morpheus", "residence": "zion"}

response = requests.put("https://reqres.in/api/users/1", json=user_data)
updated_user = response.json()
print(updated_user)
"""
Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla 
"""
response = requests.delete("https://reqres.in/api/users/6")
# verificar respuesta
if response.status_code == 204:
    # Se informa de eliminacion
    print(f"{response.status_code} : No content, Usuario eliminado correctamente")
else:
    # Se informa error
    print(f"Error al eliminar usuario:{response.status_code}")
    
    
    
