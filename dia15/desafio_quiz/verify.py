import preguntas as p


def verificar(alternativas, eleccion):
    """Verifica si la respuesta es correcta o incorrecta.

    Args:
        alternativas (lista): Lista de alternativas de la pregunta.
        eleccion (str): Elegir la alternativa.

    Returns:
        int: correcto , 1 si la respuesta es correcta, 0 Respuesta incorrecta.
    """
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)

    # generar lógica para determinar respuestas correctas

    if (alternativas[eleccion][1] == 1):
        correcto = True

        print("Respuesta correcta")
    else:
        correcto = False

        print("Respuesta incorrecta")
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta

    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)

