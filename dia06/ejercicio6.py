"""
Control de Flujo

condicional IF

Si se cumpple la condicion, entonces se ejecuta el codigo

if condicion:
    # codigo a ejecutar es verdadero    
elif:
    # código que se ejecutará SÓLO SI se cumple la condición
    
else:     
    # código que se ejecutará si NO se cumple la condición

"""

edad = int(input("ingrese su edad : \n"))
if edad >= 18:
    
    print("Eres mayor de edad")
elif edad == 18:
    
    print("Tienes 18")    
    
else:
    
    print("Eres menor de edad")   
    
if edad == 0:
    print("La edad es cero") 
    
elif edad%2 == 0:
    
    print("La edad es par")    
    
else:
    print("La edad es impar")     
    
print("El programa ha finalizado")    




