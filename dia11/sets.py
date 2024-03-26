""" 
SETS : conjunto de datos, que no permite duplicados, , por lo que si se necesita conocer sólo valores únicos, esta es la estructura de datos a utilizar.
"""

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales) 
for elemento in muchos_animales:
    print(elemento)
muchos_animales.add("Chancho")
print(muchos_animales) 
muchos_animales.remove("Gato")
print(muchos_animales)  
muchos_animales.discard("Leon")
print(muchos_animales)
muchos_animales.pop()   
print(muchos_animales) 
muchos_animales.clear()
print(muchos_animales) 


"""
Solo se muestra una vez por cada ejecutar

{'Hamster', 'Tortuga', 'Erizo de Tierra', 'Hurón', 'Gato', 'Perro'}
Hamster
Tortuga
Erizo de Tierra
Hurón
Gato
Perro
{'Hamster', 'Tortuga', 'Erizo de Tierra', 'Hurón', 'Gato', 'Chancho', 'Perro'}
{'Hamster', 'Tortuga', 'Erizo de Tierra', 'Hurón', 'Chancho', 'Perro'}
{'Hamster', 'Tortuga', 'Erizo de Tierra', 'Hurón', 'Chancho', 'Perro'}
{'Tortuga', 'Erizo de Tierra', 'Hurón', 'Chancho', 'Perro'}
set() 
"""