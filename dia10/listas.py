"""
LISTAS

[]   listas         Son contenedores que permiten almacenar múltiples datos,  son mutables   a = [1, 2, 3, 4] Son todo lo que esté dentro de los corchetes [], separados por coma

()   duplas
{}   diccionarios

"""


# Mostrar una lista
a = [1, 2, 3, 4]    # tamaño de la lista es 4
print(a) # mostramos los valores de la lista a definida arriba
print([1, 2, 'hola', 4]) # mostramos directo una lista

# Índice     #En una lista que contiene 4 elementos: el primer elemento está en la posición cero, el último en la posición 3.

colores = ["verde", "rojo", "rosa", "azul"]   
print(len(colores))  # el tamaño es 4
print(colores[0])  # verde
print(colores[1])  # rojo
print(colores[3])  # azul
# print(colores[8])   # IndexError: list index out of range

print(colores[-1])  # muestra el ultimo elemento de la lista  # azul
print(colores[-2])  # muestra el penultimo                    # rosa

lista_pares =[2, 4, 6, 8 ,10]
lista_vacia =[]

#METODOS

print(lista_pares.__dir__)   #  <built-in method __dir__ of list object at 0x0000027A2A831F40>

print(lista_pares.__dir__())  # muestra todas las funciones que tenemos con los objetos

# Método append(x)   #append(datos)  agregar un elemento al final de la lista

lista_vacia.append("Lunes")
print(lista_vacia)           # muestra ['Lunes']

lista_vacia.append("Martes")
lista_vacia.append("Miercoles")
print(lista_vacia)           # ['Lunes', 'Martes', 'Miercoles']

# Método insert(i,x)     Agrega el elemento x en la posición i específica

lista_vacia.insert(3,"jueves")
lista_vacia.insert(3,"Viernes")   
print(lista_vacia)                  # ['Lunes', 'Martes', 'Miercoles', 'Viernes', 'jueves']  

lista_vacia.insert(10,"Sabado")
print(lista_vacia)                  # ['Lunes', 'Martes', 'Miercoles', 'Viernes', 'jueves', 'Sabado']

# Método pop()  Sacar el último elemento dentro de una lista

lista_eliminados = []
lista_eliminados.append(lista_vacia.pop(0))

lista_vacia.pop(4)
print(lista_vacia)                  # ['Lunes', 'Martes', 'Miercoles', 'Viernes', 'Sabado']  elimino jueves que estaba en la posicion  
eliminado=lista_vacia.pop(0)
print(f"El elemento eliminado {eliminado}")   # El elemento eliminado Martes
print(lista_vacia)                            # ['Miercoles', 'Viernes', 'Sabado']   
print(lista_eliminados)                       # ['Lunes']

#Método remove()  Remover un elemento específico. En caso que el elemento no esté presente en la lista, Python arrojará un error ValueError.
lista_vacia =['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']  

# lista_vacia.remove("Martes")
# print(lista_vacia)               # ValueError: list.remove(x): x not in list

# Método reverse()   Invertir el orden de los elementos de una lista

numeros = [100, 20, 70, 500]
animales = ["perro", "gato", "hurón", "erizo"]
numeros.reverse()
animales.reverse()
print(numeros)                  # [500, 70, 20, 100]
print(animales)                 # ['erizo', 'hurón', 'gato', 'perro']


lista_vacia.reverse()
print(lista_vacia)       #  ['Domingo', 'Sabado', 'Viernes', 'jueves', 'Miercoles', 'Martes', 'Lunes']  los cambios son permanentes

# Método sort()          Ordenar los elementos de forma ascendente

lista_vacia.sort()      
print(lista_vacia)       # ['Domingo', 'Jueves', 'Lunes', 'Martes', 'Miercoles', 'Sabado', 'Viernes']

animales.sort()
numeros.sort()
print(animales)          # ['erizo', 'gato', 'hurón', 'perro']
print(numeros)           # [20, 70, 100, 500]

# Respaldo de lista
lista_pares = [2, 4, 6, 8 ,10, 13]

lista1 = lista_pares  #  [2, 4, 6, 8, 10, 13]    # NO ES UN RESPALDO DE DATOS

lista2 = lista_pares.copy()                      # ES UN RESPALDO DE DATOS
lista3 = lista_pares[:]                          # ES UN RESPALDO DE DATOS
lista4 = lista_pares+ []                         # ES UN RESPALDO DE DATOS  - FORMA NO LIMPIA
lista5 = lista_pares*1                           # ES UN RESPALDO DE DATOS  - FORMA NO LIMPIA
lista6 = list(lista_pares)                       # ES UN RESPALDO DE DATOS

lista_pares.pop()
print("lista de pares",lista_pares) #  lista de pares [2, 4, 6, 8, 10]
print(lista1)                       # [2, 4, 6, 8, 10]
print(lista2)                       # [2, 4, 6, 8, 10, 13]

# sorted

# ordenamiento ascendente o descendente
sorted(lista_pares, reverse=True)
print(lista_pares)                        # no es permanente  [2, 4, 6, 8, 10]
print(sorted(lista_pares, reverse=True))  # [10, 8, 6, 4, 2]  descendente

# Método index()  Retorna el índice (de cero al que corresponda dependiendo del largo de la lista)

print(animales.index('gato'))    # 1   posiscion, cuidado, solo buscar valores que existen

print(numeros.index(500))        # 3   posiscion

# OPERACIONES

# Concatenación de listas

animales = ['Gato', 'Perro', 'Tortuga']   # definamos dos listas de animales
animales_2 = ['Hurón', 'Hamster', 'Erizo de Tierra']

mascotas = animales + animales_2          # Si las concatenamos, podremos obtener una lista de mascotas

print(animales)                        # ['Gato', 'Perro', 'Tortuga']
print(len(animales))                   # 3
print(animales_2)                      # ['Hurón', 'Hamster', 'Erizo de Tierra']     
print(len(animales_2))                 # 3
print(mascotas)                        # ['Gato', 'Perro', 'Tortuga', 'Hurón', 'Hamster', 'Erizo de Tierra']
print(len(mascotas))                   # 6

# Repitiendo listas

animales_actualizados = animales * 4                     
mascotas = animales_actualizados + animales_2            
print(animales_actualizados)                    # ['Gato', 'Perro', 'Tortuga', 'Gato', 'Perro', 'Tortuga', 'Gato', 'Perro', 'Tortuga', 'Gato', 'Perro', 'Tortuga']
print(len(animales_actualizados))               # 12
print(animales_2)                               # ['Hurón', 'Hamster', 'Erizo de Tierra']
print(len(animales_2))                          # 3
print(mascotas)                                 # ['Gato', 'Perro', 'Tortuga', 'Gato', 'Perro', 'Tortuga', 'Gato', 'Perro', 'Tortuga', 'Gato', 'Perro', 'Tortuga', 'Hurón', 'Hamster', 'Erizo de Tierra']
print(len(mascotas))                            # 15





