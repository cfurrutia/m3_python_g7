"""
Diccionarios   {}

Estructura de datos compuesta por pares de clave:valor, donde :
Cada clave se asocia con un elemento del diccionario
○ Como toda estructura de datos, permiten almacenar una gran cantidad de datos 
en una sola variable.
las claves no se generan automaticamente, no hay un orden  
pueden ser String, numericos, incluso booleanos.

si la clave existe se modifica y si n oexiste lo agrega.
"""
# Listas vs Diccionarios

lista = [25, 31, "hola"]  # En una lista usamos la posición para acceder a un elemento, y los índices se generan en forma implícita
lista[2] # "hola"

diccionario = {1:"uno","dos":2, 3: ("a", "b", "c")}  # En un diccionario usamos la clave, y se deben definir de forma explícita

# ejemplo

# notas = {"Camila": 7, "Antonio": 5, "Felipe": 6, "Antonia": 7}

notas = {
"Camila": 7,
"Antonio": 5,
"Felipe": 6,
"Daniela": 5,
"Vicente": 7,
"FELIPE": 4,             # AGREGADO DESPUÉS PARA EJEMPLO (ELIMINAR)
}

print(len(notas))  # 6
print(notas)       # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'FELIPE': 4}

# Acceso a los elementos(valores)
print(notas["Camila"])   # 7   para obtener el valor, debemos tener acceso atraves de la clave
# print(notas["felipe"]) # KeyError: 'felipe'


notas["Julio"] = 4
print(notas)             # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'FELIPE': 4, 'Julio': 4}

# modificar por clave:valor
notas["Julio"] = 5
print(notas)             # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'FELIPE': 4, 'Julio': 5}

# Eliminar par clave:valor

del notas ["FELIPE"]
print(notas)             # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5}

# 2 formar pop()  --> al eliminar, capturamos el valor
eliminando = notas.pop("Camila") # notas ["Camila"]
print("Valor eliminado :", eliminando)                  # Valor eliminado : 7
print(notas)                                            # {'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5}

# Unir diccionarios
notas2 ={"Mijail":2,"Israel":1}

notas.update(notas2)
print(notas)                                  # {'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7, 'Julio': 5, 'Mijail': 2, 'Israel': 1}

# ¡Cuidado con las colisiones!  Cuando ambos diccionarios tienen una clave en común, 
# el valor del segundo diccionario sobreescribe al del primero.

diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
diccionario_b = { "mascota":"miti", "ejercicio":"bicicleta", "altura": 155}
# Union de diccionario_a y diccionario_b
diccionario_a.update(diccionario_b)
# Se sobreescribió el valor de altura por el del diccionario_b
print(diccionario_a)                          # {'nombre': 'Alejandra', 'apellido': 'López', 'edad': 33, 'altura': 155, 'mascota': 'miti', 'ejercicio': 'bicicleta'}