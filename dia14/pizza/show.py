def mostrar_ingredientes(ingredientes):
    print(f'Su masa es: {ingredientes["masa"]}')
    print(f'Su salsa es: {ingredientes["salsa"]}')
    print('Los ingredientes de su Pizza:')
    for ing in ingredientes['ingredientes']:
        print(f'- {ing}')