#Actividad 2 - Rentabilidad



# Solicitar valores al usuario
psuscripcion = float(input("Ingrese el precio de Suscripción: \n")) #[pesos/persona]  
numero_usuario = int(input("Ingrese el número de Usuarios:  \n"))  # [persona]
gasto_total = float(input("Ingrese el gasto total: \n"))  # [pesos]

# Calcular utilidades
utilidades = psuscripcion * numero_usuario - gasto_total # [pesos]

# Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades} pesos")

