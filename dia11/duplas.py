"""
Tuplas : conjunto de datos ordenados e inmutables, se escriben con parentesis ()

Una propiedad útil es lo que se llama unpacking o desempaquetamiento:Par ordenado inmutable 
No se pueden modificar partes de ella, en caso de querer actualizarlo se debe modificar la tupla completa
"""

tupla1 = (1,3,5,7,9)
print(tupla1)                 # (1, 3, 5, 7, 9)
print(type(tupla1))           # <class 'tuple'>
tupla2 =("nombre","Mijail")

nom, texto = tupla2
print(nom)           # nombre
print(texto)         # Mijail
print(tupla2[0])     # nombre
print(tupla2[1])     # Mijail

# nose puede  INMUTABLES
# print(tupla2[2])   # IndexError: tuple index out of range
# tupla2[2] = "hola" # TypeError: 'tuple' object does not support item assignment

# ITERAR TUPLA

for num in tupla1:
    print(num)       # 1  3   5  7  9
    
# print({"nota1":5,"nota2":6}.items())    # dict_items([('nota1', 5), ('nota2', 6)])

list_dicc1 = list({"nota1":5,"nota2":6}.items())   # dict_items([('nota1', 5), ('nota2', 6)])  
print(list_dicc1)                                  # [('nota1', 5), ('nota2', 6)]           
print(list_dicc1[0])                               # ('nota1', 5)
print(list_dicc1[1])                               # ('nota2', 6)
print("")

print(list_dicc1[0][0])                            # nota1
print(list_dicc1[0][1])                            # 5
