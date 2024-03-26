# Filtrado
"""
A continuación, se muestra cómo crear un programa que filtre todos los números 
de una lista que sean menores a 1000. Esto es lo mismo que decir "seleccionar 
todos los elementos mayor o iguales a mil".
Transformarlo en un List Comprehension
"""
a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)

filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

# comprehension
filtered_array2 =[a[i] for i in range(n) if a[i] >= 1000 ]
print(filtered_array2)


# Adicto a redes
"""
Se tiene una lista con la cantidad de minutos usados en redes sociales de distintos 
usuarios.
Se debe retornar una lista que clasifique todos los tiempos menores a 90 minutos 
como 'bien' y todos los tiempos mayores o iguales a 90 como 'mal'.
El output debería ser algo similar a lo siguiente:
[120, 50, 600, 30, 90, 10, 200, 0, 500]
['mal', 'bien', 'mal', 'bien', 'bien', 'bien', 'mal', 'bien', 'mal'] 
"""
cantidad_minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]

separador =[]
for tiempo in cantidad_minutos:
    if tiempo < 90:
        separador.append('bien')
    else:
        separador.append('mal') 
print(separador)

# comprehension
separador2=['bien'if tiempo < 90 else 'mal' for tiempo in cantidad_minutos]        
print(separador2)


# Transformando segundos a minutos
"""
Se tiene una lista con la cantidad de segundos que demoraron algunos procesos.
Se necesita una función para transformar todos los datos a minutos, (se requiere 
sólo la parte entera, la parte decimal se puede ignorar).
seconds = [100, 50, 1000, 5000, 1000, 500]
"""

segundos = [100, 50, 1000, 5000, 1000, 500]
minutos = []
for pasarAminutos in segundos:
       minutos.append(pasarAminutos // 60)  
print("Lista de segundos convertida a minutos :", minutos)

# comprehension
minutos2 =  [pasarAminutos // 60 for pasarAminutos in segundos] 
print("Lista de segundos convertida a minutos :", minutos2)


# Países
"""
Tenemos un listado de países y la cantidad de usuarios por cada país en la 
siguiente tabla:

País       Cantidad de usuarios
México             70
Chile              50
Argentina          55

1. Convertir la tabla mostrada en un diccionario.
2. Filtrar los países con menos de 60 usuarios.
"""

listadopaises = {"México": 70, "Chile": 50, "Argentina": 55}
for pais, usuarios in listadopaises.items():
    if usuarios >= 60:
        print(f"Pais {pais} tiene {usuarios} usuarios")

# comprehension    
print({pais: usuarios for pais, usuarios in listadopaises.items() if usuarios >= 60})


# Ventas
"""
Dada la información de ventas de 3 meses:

Mes         Ventas
Octubre     65000
Noviembre   68000
Diciembre   72000

1. Convertir la tabla en un diccionario
2. Modificar el diccionario para incrementar las ventas en un 10%.
3. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%
"""
ventas_mensuales = {"Octubre": 65000, "Noviembre": 68000, "Diciembre": 72000}

ventas_incrementadas = {mes: ventas * 1.10 for mes, ventas in ventas_mensuales.items()}
print(ventas_incrementadas)

# ventas_disminuidas = {mes: (ventas * 1.10)*0.80 for mes, ventas in ventas_mensuales.items()}
ventas_disminuidas = {mes: ventas *0.80 for mes, ventas in ventas_mensuales.items()}
print(ventas_disminuidas)

    