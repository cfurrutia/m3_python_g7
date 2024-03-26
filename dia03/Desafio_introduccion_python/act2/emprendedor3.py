#Actividad 2 - Rentabilidad


# Solicitar valores al usuario
psuscripcion = float(input("Ingrese el precio de Suscripción:\n")) # [pesos/persona] 
nusuario_nomral = int(input("Ingrese el número de usuarios nomrales: \n")) # [persona]
gasto_total = float(input("Ingrese el gastos total de este año: \n")) # [pesos] 
utilidades_anterior = float(input("Ingrese utilidades del año anterior \n")) # [pesos] 

# Calcular utilidades
utilidades_actuales = psuscripcion * nusuario_nomral - gasto_total 

# Mostrar el resultado de las utilidades
print(f"Las utilidades del proyecto son: {utilidades_actuales} pesos") # [pesos]


# calcular la razón entre las utilidades actuales y las del año anterior
razon = utilidades_actuales/utilidades_anterior

# Mostrar el cálculo de la razón 
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f} ")
