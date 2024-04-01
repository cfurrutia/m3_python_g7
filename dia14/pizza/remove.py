def quitar_ingrediente(ingredientes, eleccion):
    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla',
    'Pollo','Jamón','Carne','Tocino','Queso']
    quitar = disponibles[eleccion-1]

    if quitar in ingredientes['ingredientes']:
        ingredientes['ingredientes'].remove(quitar)
        print(f'Se ha quitado {quitar}')
    elif len(ingredientes['ingredientes']) == 0:
        print('No hay ningún ingrediente que quitar')
    else:
        print('No se puede quitar ese ingrediente, porque no está incluido') 

    return ingredientes
