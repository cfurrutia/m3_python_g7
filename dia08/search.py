"""
Búsqueda
Es muy común tener que buscar un elemento específico en la estructura 
contenedora. Uno podría almacenar el elemento buscado y terminar de recorrer los 
elementos sin uso de break, pero esto no tiene mucho sentido, ya que puede ser 
muy costoso el recorrer estructuras de datos muy grandes si es que ya se encontró 
lo que se busca. 
En este caso buscaremos por un número y diremos en qué posición se encontraba. 
"""

import sys, random

numero_buscar = int(sys.argv[1]) # número a buscar # número a buscar

lista = [1,2,3,4,5,6,7,8,9,0]
# .shuffle de la librería random permite mezclar
# la lista de dígitos para aumentar un poco la dificultad.
random.shuffle(lista) # desordenar la lista, de forma permanente ejem  lista = [4,7,3,1,5,6,2,8,0,9]
print(lista)

for posicion, numero in enumerate(lista):
    
    if numero_buscar == numero:
        print("Numero enc0ntrado")
        break
    
    else:
# Si es que no es el elemento buscado lo reportamos
        print(f"Elemento no encontrado en la posicion {posicion}")


print("fuera del for") 
print(f"El numero {numero_buscar} se encontro en la posición {posicion}")   






