
"""
Actividad 1 calcular el IMC de una persona y guiados por la OMS a determinar  a que clasificacion pertece
deacuerdo al rango de los datos ingresados.

"""
# Ingreso del peso del usuario
peso_en_kg = float(input("Ingrese su peso en Kg: "))

# validacion del peso
if peso_en_kg <= 0:
    print("Error el peso debe ser mayor a cero !!!")

    peso_en_kg = float(input("Ingrese su peso en Kg: "))
    
# Ingrese la altura
altura_centimetros = float(input("Ingrese su altura en centímetros: "))

# validacion de la altura
if altura_centimetros <= 0:
    print("Error la altura debe ser mayor a cero !!!")

    altura_centimetros = float(input("Ingrese su altura en centímetros: "))

# calcular el indice de masa corporal
imc = peso_en_kg / ((altura_centimetros / 100)**2) 

# Clasificación OMS Bajo Peso
if imc < 18.5:
    print(f"Su imc esta en el rango es : {imc:.2f} clasificación es bajo de peso ")

# Clasificación OMS Adecuado
elif 18.5 <= imc < 25:
    print(f"Su imc esta en el rango es : {imc:.2f} clasificación es Adecuedo ")

# Clasificación OMS Sobrepeso
elif 25 <= imc < 30:
    print(f"Su imc esta en el rango es : {imc:.2f} clasificación es Sobrepeso ")

# Clasificación OMS Obesidad Grado I
elif 30 <= imc < 35:
    print(f"Su imc esta en el rango es : {imc:.2f} clasificación es Obesidad Grado I")

# Clasificación OMS Obesidad Grado II
elif 35 <= imc < 40:
    print(f"Su imc esta en el rango es : {imc:.2f} clasificación es Obesidad Grado II")

# Clasificación OMS Obesidad Grado III
else:
    print(f"Su imc esta en el rango es : {imc:.2f} clasificación es Obesidad Grado III")