#esto es una linea de comentario

"""
comentario
de mas de
una linea
"""

print("Estamos trabajando con vscode")
print(2+2)
print(24-2)
print(12/3)
print(12/2)
print(7*3)

#print(7/0)  # ZeroDivisionError: division by zero

numero =36
print(numero)

#no esta permitido la suma de letras y numeros

#INTERPOLACION
print(f"el numero es {numero}")

#print(f"el numero es {numero+2}")  tambien se puede hacer una suma

nombre = "Carlos"
print(f"tu nombre es {nombre} y tu edad es {numero}")
print(f"tu nombre es {nombre} \n y tu edad es {numero}")

#todas estas son variantes, pero la forma de arriba es la mas actual
#####################################################################
print("tu nombre es "+nombre)
#string.format
print("tu nombre es {} y tu edad es {}".format(nombre,numero))
# formato con %:  %s para string y %d para numeros
print("tu nombre es %s y tu edad es %d" % (nombre,numero))
#####################################################################

#metodo con cadena
apellido = "urrutia"
print(apellido.title())
