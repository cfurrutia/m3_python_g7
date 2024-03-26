
"""
# Ejercicio

¡Practiquemos!
1. Crea un diccionario
2. Agrega un elemento
3. Cambia un elemento
4. Elimina un elemento 


#1 Crea un diccionario
altura_estudiantes ={"Pedro": 167,"Juan": 171,"Diego": 172,"Carolina": 164,"Claudia": 168,"Alejandro": 187,"Ana": 172,"Claudio": 162}  # cm
print(altura_estudiantes)                                 # {'Pedro': 167, 'Juan': 171, 'Diego': 172, 'Carolina': 164, 'Claudia': 168, 'Alejandro': 187, 'Ana': 172, 'Claudio': 162}

#2 Agrega un elemento
altura_estudiantes["Cesar"] = 164
print(altura_estudiantes)                                # {'Pedro': 167, 'Juan': 171, 'Diego': 172, 'Carolina': 164, 'Claudia': 168, 'Alejandro': 187, 'Ana': 172, 'Claudio': 162, 'Cesar': 164}

#3 Cambia un elemento
altura_estudiantes["Diego"] = 174
print(altura_estudiantes)                                # {'Pedro': 167, 'Juan': 171, 'Diego': 174, 'Carolina': 164, 'Claudia': 168, 'Alejandro': 187, 'Ana': 172, 'Claudio': 162, 'Cesar': 164}

#4 Elimina un elemento 
borrar_estudiante = altura_estudiantes.pop("Alejandro")  
print("Borrar datos:", borrar_estudiante)                # Borrar datos: 187               
print(borrar_estudiante)                                 # 187
print(altura_estudiantes)                                # {'Pedro': 167, 'Juan': 171, 'Diego': 174, 'Carolina': 164, 'Claudia': 168, 'Ana': 172, 'Claudio': 162, 'Cesar': 164}  

# FIN DE EJERCICIO
"""
from os import system

mascotas = {}

cant_mascotas = int(input("Ingrese cantidad de mascotas a ingresas"))#3

""""""
for i in range(cant_mascotas):#0,1,2
    
    mascota = {
        "nombre":"",
        "raza":"",
        "peso":0.0,
        "chip": False,
    }

    #Recorrer un diccionario default
    """for clave in mascota:
        #print(clave)
        mascota[clave] = input(f"Ingrese la {clave} de su mascota> ")
    """

    for key in mascota.keys():
        #print(key)
        mascota[key] = input(f"Ingrese la {key} de su mascota> ")

    print(mascota)

    print("")
    
    # Método values() Entrega una lista con todos los valores de un diccionario
    for valor in mascota.values():
        print(valor)

    print("")
    
    # Método items()  Entrega una lista con los pares clave-valor de un diccionario
    for clave,valor in mascota.items():
        print(f"clave {clave} - valor {valor}")


    mascotas[mascota["nombre"]] = mascota
    #mascotas["zoe"] = mascota


print(mascotas)#
{
    'Zoe': {'nombre': 'Zoe', 'raza': 'bull', 'peso': '9', 'chip': 'si'}, 
    'ayun': {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'}, 
    'negrito': {'nombre': 'negrito', 'raza': 'chilenzis', 'peso': '30', 'chip': 'si'}
}

#acceder a un diccionario dentro de un diccionario
#mascotas["ayun"]            => {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'}
#mascotas["ayun"]["nombre"]  => "ayun"

#mascotas["ayun"].pop("nombre")

"""
mascotas ={
    1: {'nombre': 'zoe', 'raza': 'bull', 'peso': '9', 'chip': 'si'},
    2: {'nombre': 'ayun', 'raza': 'bull', 'peso': '12', 'chip': 'si'},
    
}
"""
"""
# Método items() Entrega una lista con los pares clave-valor de un diccionario

computador = {'notebook': 489990, 'tablet': 120000, 'cargador': 12400}
computador.items()
# dict_items([('notebook', 489990), ('tablet', 120000), ('cargador', 12400)])

# Método get()  Entrega un mensaje alternativo en caso de no encontrar alguna clave
computador = {'notebook': 489990, 'tablet': 120000, 'cargador': 12400}
computador.get('notebook', 'No se encuentra el elemento solicitado')
#  none 'No se encuentra el elemento solicitado'

"""