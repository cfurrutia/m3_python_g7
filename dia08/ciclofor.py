"""
ciclo for

for variable in iterable: 

"""
# Con un sólo valor
for i in range(10):
    print(i)
    
print("")

# Con dos valores
for i in range(4,10):
    print(i)
    
# Con tres valores
for i in range(4,10,2):
    print(i)
    
"""
ejemplo en javascrip
for (let index = 4; index < 10; index++) {
    console.log(index);
}
"""    
# listas
print("")
numeros=[2,"4",True,3,"5"]
for numero in numeros:
    print(numero)    

# string    
texto = "hola mundo"
for caracter in texto:
    print(caracter)    
    
# diccionario  

datos_personales={
    "Nombre": "Israel",
    "Apellido": "Palma",
    "edad": 44,
}  
# imprimir las claves
for clave in datos_personales:
    print(clave)


print("")

# imprimir los valores
for clave in datos_personales:
    print(datos_personales[clave])
    
    
# imprimir clave y valor    
for clave,valor in datos_personales.items():
    print(f"clave : {clave} - valor : {valor}")
    
print("")    
    
for par in datos_personales.items():
    print(par)   
    
print("")       
    
for clave in datos_personales.keys():
    print(clave)  
    
print("")         
    
for valor in datos_personales.values():
    print(valor)                    

# enumerate()  Permite agregar un contador a la iteración, por lo tanto extrae elemento y contador.

texto = "Esternocleidomastoideo"
for posicion, caracter in enumerate(texto):
    print(f"La letra en la posición {posicion} es el {caracter}")

print("")       
for posicion, numero in enumerate(numeros):
    print(f"La letra en la posición {posicion} es el {numero}")
    
# zip()  funciona cuando tiene la misma cantidad alamacenada, Permite unir varios iterables para utilizarlos dentro de la misma iteración.

prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}')      
    
print("")  

# break, hace que el ciclo termine y se continúe con la ejecución del resto del programa
numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]

for numero in numeros:
    print(numero)
    if numero ==3:
        break
print("Fuera del for")    

