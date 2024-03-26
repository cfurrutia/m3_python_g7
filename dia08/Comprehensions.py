
"""
Transformando un ciclo for en un Comprehension

Supongamos el siguiente problema: queremos generar los 10 primeros números pares y 
almacenarlos en una lista: 
"""

# solicitamos el número de pares a generar
n = 10

# generamos una lista vacía para almacenar los pares, de tamaño cero
lista_pares = []

for i in range(n):
    lista_pares.append(2*i + 2)  # podemos hacer append de los valores generados (agrega elementos al final de la lista), en este caso partimos desde el 2
    
"""
for i in range(1,n+1):
    lista_pares.append(2*i)  
"""
"""
for i in range(2,n+2):
    lista_pares.append(i)  
"""

# mostramos el resultado
print(lista_pares)  # Muestra [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# [fórmula for variable in iterable]  #  for variable in range(n):
lista_pares2 =  [2*i + 2 for i in range(n)] 
print(lista_pares2)

# Condicionales con List Comprehensions

valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)


divisibles2=['Divisible' if valor %2 == 0 else 'No divisible' for valor in valores]
print(divisibles2)

# Operaciones de filtrado
lista = ['Lechugas', 'Tomates', 5, 10,True, False, True, 'Papas',5.1, 45.2, 1, 2, 0]
lista_str =[]
lista_int =[]
count_str = 0
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
    elif type(elemento) is int:
        lista_int.append(elemento)

print(count_str)
print(lista_str)
print(lista_int)

lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))
print(lst_str)

# diccionario comprehesion

claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
print({k:v for k,v in zip(claves, valores)})

{'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 33, 'altura': 1.75}


