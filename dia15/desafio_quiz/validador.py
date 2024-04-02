"""
 Se pide crear la función validate(), la cual debe aceptar como argumentos una lista 
de opciones y una elección.  
"""

def validate(opciones, eleccion):
    """Válida si la elección del usuario está en la lista de opciones válidas

    Args:
        opciones (str): validacion  si quiere jugar o salir del programa
        eleccion (str): ingreso de eleccion

    Returns:
        str :retorna la elección válida
    """
    # Definir validación de eleccion
    while eleccion not in opciones:
        print('Opción no válida, ingrese una de las opciones válidas: ' )
        eleccion = input('Ingresa una Opción: ').lower()

    return eleccion


if __name__ == '__main__':

    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)


