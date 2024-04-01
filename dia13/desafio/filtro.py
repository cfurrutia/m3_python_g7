"""
1. Filtrado relevante

La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al 
problema. Dada una muestra de los productos que actualmente se encuentran disponibles en la tienda (un diccionario), se solicita implementar una función que permita entregar lo 
siguiente:

Un diccionario con los productos que cumplen una cierta condición dado un umbral

La función debe permitir mostrar los valores mayor que o menor que un umbral (siempre estrictos).

Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos que se indique lo contrario
"""
import sys
# primer argumento de entrada
umbral = int(sys.argv[1])  
# Precios de los artículos
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}
# funcion para filtrar cuando solo se ingresa umbral sin opcion
def filtrar(precios, umbral):
    productos_filtrados = {productos: valor for productos, valor in precios.items() if valor > umbral}
    return productos_filtrados

# funcion cuando se ingresa umbral con opcion mayor o menor
def filtrar2(precios, umbral, opcion):
    if opcion == "menor":
        productos_filtrados = {productos: valor for productos, valor in precios.items() if valor < umbral}
    elif opcion == "mayor":
        productos_filtrados = {productos: valor for productos, valor in precios.items() if valor > umbral}
    else:
        return None
    
    return productos_filtrados

# condiciones y llamada a las funciones

if len(sys.argv) == 3:
    # Segundo argumento de entrada
    opcion = sys.argv[2]
    resultado = filtrar2(precios, umbral, opcion)
    
    if resultado is not None:
        if resultado:
            print(f'Los productos {opcion}es al umbral son: {", ".join(resultado)}')
        else:
            print(f'No se encontraron productos {opcion}es al umbral.')
    else:
        print(f'Lo sentimos, {opcion} no es una operación válida.')
elif len(sys.argv) == 2:
    resultado = filtrar(precios, umbral)
    print(f'Los productos mayores al umbral son: {", ".join(resultado)}')

else:
    print('Lo sentimos, la opcion no es una operación válida.')   