"""
while condicion:
    #codigo a ejecutar    
    
"""
import getpass

"""
password = getpass.getpass("Ingrese la clave secreta: \n")

while len(password) < 6:
    password = input("no adivinaste la contraseña con el largo superior a 6 caracteres \n")

while password !="Hola Mundo":
    password = input("no adivinaste la contraseña, Ingrese su contraseña nuevamente : \n")

print("Contraseña correcta")
print("Fin del programa")    
"""
# iteracion
"""
i = 0
while i < 10:
    print(f"El valor de i es : {i}")
    i = i+1   # incremento en 1
    
print("Fuera del while") 
"""

"""
saludo = "Hola"
saludo = saludo + "Mundo"
print(saludo)
saludo += "chao"
print(saludo)
"""

# sumando de 1 a 100

i = 1 # primer valor a sumar
suma = 0
while i <= 100:
    suma += i    # acumulamos para la suma
    i += 1       # incrementamos para sumar el siguiente valor

print(f"El resultado final es {suma}")
