#operacion de suma

"""sumanr dos numeros enterors ingresados por el usuario
mostrar el resultado de la suma

inicio
    leer numero1
    leer numero2
    opratorio numero1+numero2
    mostrar numero1+numero2
fin
"""

numero1 = int(input("ingrese el primer numero : "))
numero2 = int(input("ingrese el segundo numero : "))

print(f"El resultado de la suma es : {numero1 + numero2}")

# area del rectangulo

base = float(input("Ingresa la base del rectangulo : "))
altura = float(input("Ingrese la altura del rectangulo :"))
print(f"El rectangulo es : {base * altura}")

#solicitar al usuario en ingreso de 3 numeros y determinar cuales de ellos es mayor que 33
#solo numeros enteros 1 al 100 y determinar cual es mayor y cual es menor

"""Solicitar al usuario ingresar 3 números enteros entre 1 y 100
        Escribir "Por favor ingrese el primer número (entre 1 y 100):"
        Leer num1
        Escribir "Por favor ingrese el segundo número (entre 1 y 100):"
        Leer num2
        Escribir "Por favor ingrese el tercer número (entre 1 y 100):"
        Leer num3

    Verificar si alguno de los números es mayor que 33
    Si num1 > 33 Entonces
        Escribir "El primer número es mayor que 33."
    Fin Si
    Si num2 > 33 Entonces
        Escribir "El segundo número es mayor que 33."
    Fin Si
    Si num3 > 33 Entonces
        Escribir "El tercer número es mayor que 33."
    Fin Si

    Determinar cuál es el número mayor y cuál es el número menor
    mayor = num1
    menor = num1

    Si num2 > mayor Entonces
        mayor = num2
    Fin Si
    Si num3 > mayor Entonces
        mayor = num3
    Fin Si

    Si num2 < menor Entonces
        menor = num2
    Fin Si
    Si num3 < menor Entonces
        menor = num3
    Fin Si

    Escribir "El número mayor es: " + mayor
    Escribir "El número menor es: " + menor

Fin

    """