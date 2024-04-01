def agregar_ingrediente(ingredientes, eleccion):

    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo',
    'Jamón','Carne','Tocino','Queso']
    nuevo_ingrediente = disponibles[eleccion-1]

    if nuevo_ingrediente in ingredientes['ingredientes']:
        print('El ingrediente ya existe')
    else:
        ingredientes['ingredientes'].append(nuevo_ingrediente)
        print(f'Se ha agregado {nuevo_ingrediente}')

    return ingredientes