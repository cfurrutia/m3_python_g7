# Paso 1
def productoria(lista):
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor

# Paso 2
def factorial(n):
    valor = 1
    for elemento in range(1,n+1):
        valor *= elemento
    return valor

# Paso 3
def calcular(**parametros):
    for k, v in parametros.items():
        if 'fact' in k:
            print(f'El factorial de {v} es {factorial(v)}')
        else:
            print(f'La productoria de {v} es {productoria(v)}')

# Paso 4
calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)