
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

# uso startswith

def calcular(**elementos):
    for clave,valor in elementos.items():
        
        if  clave.startswith("fact"):  
            print(f"El factorial de {valor} es {fact_i(valor)}")
        elif clave.startswith("prod"):  
            print(f"La productoria de {valor} es {prod_i(valor)}")

calcular(fact_1 = 5, prod_1=[4,6,7,4,3], fact_2=6)
