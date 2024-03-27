
"""
Genere un archivo llamado word_count.py que importe un texto a Python y realice las siguientes tareas:

Utilizando una estructura de datos apropiada, cuente la cantidad de caracteres 
distintos que componen un texto.

Cuente el número de palabras distintas que componen el texto ingresado. Para 
separar un texto por espacios puede utilizar el método .split("").
"""
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()                                         # Lee el contenido del archivo 

caracteres_distintos = set(texto)                               # Encontrar los caracteres distintos
contador_caracteres = len(caracteres_distintos)                 # Contar los caracteres distintos 

separar_palabras = texto.split(" ")                             # Separar un texto por espacios 
palabras_distintas = set(separar_palabras)                      # Encontrar las palabras distintas
contador_palabras = len(palabras_distintas)                     # Contar las palabras distintas

print(f"El numero de caracteres distintos es: {contador_caracteres}")  # Mostrar el numero de caracteres distintos
print(f"El numero de palabras distintas es: {contador_palabras}")      # Mostrar el numero de palabras distintas