"""
Crear un programa llamado shuffle.py que contenga la función shuffle_alt().

Esta función debe tomar como argumento una pregunta desde el archivo 
preguntas.py (con un nivel y una pregunta definida) y mezclar las alternativas.

La función debe retornar las alternativas mezcladas. 
"""
import preguntas as p
import random

def shuffle_alt(pregunta):
    """Mezcla las alternativas de cada pregunta

    Args:
        pregunta (diccionario ): alternativas con su pregunta

    Returns:
        lista: alternativas mezcladas de las preguntas
    """
    #mezclar alternativas

    random.shuffle(pregunta['alternativas'])    
    return pregunta['alternativas']

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]