"""
Cree un programa llamado level.py que incluya la función choose_level() que permite 
escoger el nivel de dificultad de la pregunta a realizar. 

Esta función debe aceptar como argumentos el número de la pregunta, y la cantidad 
de preguntas por nivel que puede ser 1, 2 o 3. 
El funcionamiento debe ser el siguiente:

Si se eligen 2 preguntas por nivel
Las preguntas n°1 y n°2 deben ser de nivel de dificultad básicas.
Las preguntas n°3 y n°4 de nivel intermedio 
Y las preguntas n°5 y n°6 avanzadas. 
En cambio si se escogen 3 preguntas por nivel la 1,2 y 3 deben ser básicas, 4,5,6 intermedias y 7, 8 y 9 avanzadas.
La función debe retornar el nivel escogido 
"""
def choose_level(n_pregunta, p_level):
    """Elige el nivel de dificultad de la pregunta a realizar

    Args:
        n_pregunta (int): numero de preguntas
        p_level (int): cantidad de preguntas por nivel 

    Returns:
        str:  retornar el nivel escogido
    """

    # Construir lógica para escoger el nivel


    if n_pregunta<= p_level:
        level = 'basicas'
    elif n_pregunta<= 2*p_level:
        level = 'intermedias'     
    else:
        level = 'avanzadas'    

    return level          

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias