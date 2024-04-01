def tipo_masa(ingredientes, eleccion):
    if eleccion == 'T':
        ingredientes['masa'] = 'Masa Tradicional'
    elif eleccion == 'D':
        ingredientes['masa'] = 'Masa Delgada'
    elif eleccion == 'B':
        ingredientes['masa'] = 'Masa con Bordes de Queso'

    if eleccion in ['T','D','B']:
        print(f'Su masa se cambió a {ingredientes["masa"]}')
    else:
        print('No se ha cambiado su tipo de Masa')

    return ingredientes

