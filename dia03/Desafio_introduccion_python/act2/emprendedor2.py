#Actividad 2 - Rentabilidad


# Solicitar valores al usuario
psuscripcion = float(input("Ingrese el precio de Suscripción:\n")) # [pesos/persona] 
nusuario_nomral = int(input("Ingrese el número de usuarios nomrales: \n")) # [persona]
nusuario_premium = int(input("Ingrese el número de usuarios premium: \n")) # [persona]
gasto_total = float(input("Ingrese el gasto total: \n")) # [pesos]

# Calcular utilidades
utilidades = (psuscripcion * nusuario_nomral  + psuscripcion * 1.5 * nusuario_premium) - gasto_total # [pesos]


# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades} pesos")


