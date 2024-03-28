def imprimir_menu():
    print('Opciones')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

def imprimir_respuestas ():
    
    
    for i in range(len(respuestas)):    # #[0,1,2] len(respuestas)=3
        print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')
    """    
    for posicion, respuesta in enumerate(respuestas):
        print(f'La respuesta a la pregunta {posicion+1} fue {respuestas}')
            
    """
preguntas = ['Enunciando pregunta 1', 'Enunciado pregunta 2', 'Enunciado pregunta 3']
respuestas = []

for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input('>'))    

print("")
imprimir_respuestas()