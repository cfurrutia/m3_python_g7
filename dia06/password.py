
"""
Crear un programa donde el usuario debe ingresar un password en la plataforma. 

Si el password tiene menos de 6 letras, se debe mostrar el aviso:

“El password es demasiado corto”
"""

# import getpass
# password=getpass.getpass("Ingrese su contraseña: ")   /  es para econder la contraseña


password=input("Ingrese su contraseña: ")

if password == "12345":
    print("El password es incorrecto")

elif len(password) <6:  # cuenta los valores ingresados
    print("El password es demasiado corto")



