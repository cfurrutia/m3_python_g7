"""
3. Apoyo matemático.
Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda escolar 
que tiene la esta ONG se está enseñando a programar algunas operaciones avanzadas a 
niños con alto potencial pero de escasos recursos. Se quiere enseñar dos operaciones 
conocidas como el factorial y la productoria y se requiere que usted prepare una script que 
implemente esto. 

Crear un script llamado ong.py que contenga las siguientes funciones:

Una función que calcule el factorial.
Una función que calcule la productoria.
Una función que permita controlar los cálculos. Esta función se debe invocar 
de la siguiente manera
"""
# La función calcula el factorial de un número n.
def factorial(numero):
    valor = 1
    for elemento in range(1,numero+1):
        valor *= elemento
    return valor

# La función calcula el producto de los elementos en una lista.
def productoria(lista):
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor

# La función donde verifica si la clave contiene 'fact'  (**kwargs)
def calcular(**control_calculos): 
    for clave, valor in control_calculos.items():
        if 'fact' in clave:
            print(f'El factorial de {valor} es :{factorial(valor)}')
        elif 'prod' in clave:
            print(f'La productoria de {valor} es : {productoria(valor)}')
        else:
            print("Argumento ingresado es ilegible")    

# Control de cálculos


"""
calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)

def fact_i(numero):
    factorial = 1
    for i in range(numero):
        factorial=(factorial*(i+1))
    return factorial

def prod_i(lista):
    productoria = 1
    for i in range(len(lista)):
        productoria = productoria * lista[i]
    return productoria

def calcular(**elementos):
    for clave,valor in elementos.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {fact_i(valor)}")
        elif "prod" in clave:
            print(f"La productoria de {valor} es {prod_i(valor)}")

calcular(fact_1 = 5, prod_1=[4,6,7,4,3], fact_2=6)
"""