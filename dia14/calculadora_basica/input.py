def captura_datos():
    """capturar los numeros impresos

    Returns:
        tupla: par de numeros capturados
    """
    x = float(input("Ingrse el primero numero : "))
    y = float(input("Ingrse el segundo numero : "))
    return x,y

if  __name__ == "__main__":
    print(captura_datos())
