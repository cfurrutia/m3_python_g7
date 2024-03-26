import getpass
from string import ascii_lowercase

#password = getpass.getpass("Ingrese la contraseña:")
password = input("Ingrese la contraseña:").lower()

letras_minusculas = ascii_lowercase
print(letras_minusculas)
contador = 0

for caracter in password:
    print(caracter)
    for letra in letras_minusculas:
        contador+=1
        if caracter == letra:
            break

print(f" La contraseña fue forzada en {contador} intentos")