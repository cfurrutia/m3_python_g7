#Revision ejercicios

"""La velocidad de escape de un planeta se define como la mínima velocidad necesaria para 
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:
𝑉𝑒 = √2𝑔𝑟
Ve : corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s2
].
r: Corresponde al radio del planeta en [m]"""
from math import sqrt

#paso 1
#capturar y almacenar datos ingresado por el usuario
radio =input("Ingrese el radio en kilometros")

#paso 2
#transformar string en numero

#paso 3
#transformar kilometros a metros multiplicar por 1000
radio = radio * 1000  # radio =6371*10000 -> 6371000

#paso 1 para g
#captirar y alamacenar dato ingresado por el usuario
constante_gravitacional = input("Ingrese la constante gravitacional")
#9.8 -> 9.8

#paso 2
#transformar string a numero(float)
constante_gravitacional = float(constante_gravitacional)
#constante_gravitacional = float ("9.8") -> constante_gravitacional = 9.8

#calculo formula 𝑉𝑒 = √2𝑔𝑟
multiplicacion = 2 * constante_gravitacional * radio

velocidad_escape = sqrt(multiplicacion)
print(f"la velocidad de escape es {round(velocidad_escape,2)}")

