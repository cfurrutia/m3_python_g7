import requests

"""
Obtenga toda la información de los usuarios retornada por la API, guárdela en una 
variable llamada users_data e imprímala en pantalla.
"""
response = requests.get("https://reqres.in/api/users/")

if response.status_code == 200:
    # Se extraen los datos de la respuesta
    # Se informa OK
    print("OK, usuarios guardados")
    users_data = response.json()
    # Se imprimen los datos
    print(users_data)
else:
    # Se informa del error
    print(f"Error al obtener usuarios: {response.status_code}")

print("")
"""
Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el 
diccionario de respuesta en una variable llamada created_user e imprímala en 
pantalla 
"""
user_data = {"first_name": "Ignacio","job": "Profesor"}
response = requests.post("https://reqres.in/api/users/", json=user_data)
if response.status_code == 201:
    # Se extraen los datos de la respuesta
    # Se informa created
    print("Created, Usuario agregado")
    created_user = response.json()
    # Se imprimen los datos
    print(created_user) 
else:
    # Se informa del error
    print(f"Error al crear usuario: {response.status_code}")

print("")
"""
Actualice un usuario llamado morpheus para que tenga un campo llamado residence
igual a zion. Guarde el diccionario de respuesta en una variable llamada 
updated_user e imprímala en pantalla.  
"""
user_data = {"name": "morpheus", "residence": "zion"}
response = requests.put("https://reqres.in/api/users/1", json=user_data)
# verificar respuesta
if response.status_code == 200:
    # Se informa OK
    print("OK, usuario actualizado")
    updated_user = response.json()
    # Se imprimen datos 
    print(updated_user)
else:
    # Se informa  error
    print(f"Error al actualizar usuario: {response.status_code}")

print("")
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
