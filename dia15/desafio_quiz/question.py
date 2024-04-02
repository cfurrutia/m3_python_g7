"""
Crear un programa llamado question.py que permita escoger una pregunta que no se haya 
hecho durante la ejecución del programa dependiendo del nivel de dificultad.

Cree una función llamada choose_q() que tome como único argumento la dificultad 
de la pregunta.

La función debe tomar las preguntas del archivo preguntas.py de acuerdo a la 
dificultad escogida. 

La función debe escoger una pregunta de las opciones disponibles y eliminar dicha 
opción para no volverla a escoger.

La función debe retornar dos elementos separados, el primero debe ser el enunciado 
escogido y el segundo las alternativas mezcladas de acuerdo a la tarea anterior.
"""
import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.

opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}

def choose_q(dificultad):
    """Escoger una pregunta no seleccionada anteriomente de forma aleatoria

    Args:
        dificultad (str): La dificultad de la pregunta escogidas

    Returns:
        Tupla: enunciado de la pregunta y las alternativas mezcladas  pregunta['enunciado']
    """
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]

    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(opciones[dificultad])
    # eliminarla del ambiente global para no escogerla de nuevo


    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f"pregunta_{n_elegido}"]
    alternativas = shuffle_alt(pregunta)

    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')