"""
Actividad 3 - Fuerza bruta
Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en 
minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras 
posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la 
contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.

NOTA: A modo explicativo se mostrará la contraseña a buscar pero la idea es que ésta se 
ingrese de manera oculta.

python fuerza_bruta.py 
Ingrese la contraseña: gato
La contraseña fue forzada en 43 intentos 

integrantes

Carlos Urrutia curiqueo
Manuel Ruiz Uribe
Yessenia Millar  Reyes


"""
from string import ascii_lowercase
import getpass

# ingresar contraseña
password = getpass.getpass("Ingrese la contraseña: ")
intentos = 0

# operacion recorrido de contraseña y conteo
for i in range(0, len(password)):
    
    # recorrido de la lista ascii_lowercase
    for letra in ascii_lowercase:
        intentos += 1
        if password[i] == letra:
            break
# Mostrar intentos
print(f"La contraseña fue forzada en {intentos} intentos")
