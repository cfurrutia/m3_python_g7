#Actividad 1 - Velocidad de escape
#velocidad de escape = vescape,  radio del planeta = radio, constante gravitacional = constanteg 

from math import sqrt


# Ingresar los valores
radio = float(input("Ingrese el radio en Kilómetros (Km) : \n"))
constante_gravitacional = float(input("Ingrese la constante de gravitacional en (m/s^2): \n"))

#Calcular la velocidad de escape
velocidad_escape = sqrt(2 * (constante_gravitacional * 1000) * radio)  

# Mostrar el resultado
print(f"La velocidad de escape es: {velocidad_escape:.1f} [m/s]")
