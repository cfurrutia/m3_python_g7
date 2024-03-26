# estos son valores integer
print(27)
print(-5)
print(0)
print(3 + 7)
print(31 - 7)
print(4 * 8)

# estos son valores float, resultados valores decimales (flotantes) y son separados por punto
print(27.6)
print(-5.9)
print(0.0)
print(3.2 + 7.456)
print(31.5 - 7.0)
print(4.190 * 8.12)
print(9.0 / 8.1)

# estos son valores string. Para definirse como un string válido, la comilla al inicio y al final debe ser la misma.
print('hola')
print("150")
print('este es un texto más largo')

# Concatenación
print("Carlos" + "Santana")   # CarlosSantana
print("Carlos " + "Santana")  # Carlos Santana

# Duplicación
print(3 * "Carlos")  # CarlosCarlosCarlos
print(5 * "12")  # 1212121212

#
numero = 100
edad = 36
print(type(edad))  #<class 'int'>  no muestra el resultado
print(type(numero))  #<class 'int'>

#metodo count() y len()
print("Santana".count("a"))  # entrega un 3 ya que el string tiene 3 "a"
print(len("77.777.777-7"))   # el resultado es 12
print(len("77777777-7"))     # el resultado es 10

#Transforma el string a mayúsculas, minúsculas
print("Santana".upper())  # resulta en SANTANA
print("Santana".lower())  # resulta en santana

#Permite colocar mayúsculas sólo a la primera letra de cada palabra.
print("carlos santana".title())  # resulta en Carlos Santana

#join -> Permite unir muchos elementos separados por un string.
print(", ".join(["a", "b", "c"]))   # el resultado es a, b, c
print(" - ".join(["a", "b", "c"]))  # el resultado es a - b - c

#Salto de línea
print("hola\na\ntodos")  # El caracter para denotar un salto de línea es \n
"""hola
a
todos"""

#Tipo de datos, entrega el tipo declase de la variable
entero = 2
decimal = -6.5
texto = "Hola Mundo"
booleanos = True
print(type(entero))      # int      <class 'int'>
print(type(decimal))     # float   <class 'float'>
print(type(texto))       # str       <class 'str'>
print(type(booleanos))   # bool  <class 'bool'>

#ejemplo
numero2 = 200
numero2 = numero2 + 100  #numero2 = 200 + 100  <--- reasignacion (incremento)
texto = "asd"
texto = texto + ""  # texto = "asd"

#Precisión de datos
print(f'El resultado de la division es {1/9}')  # El resultado de la division es 0.11111
print(f'El resultado es {1/9:.2f}')  # El resultado es 0.11
print(f"resultado de la division {1/9:.4f}")  # resultado de la division 0.1111
print(f"resultado de la division {round(1/9,3)}")  # resultado de la division 0.111

#Ingresando datos (input)
nombre = input("ingrese su nombre : \n")
print(f"Tu nombre es {nombre}")
edad = input("ingrese su edad : \n")
print(f"Tu edad es {edad}")