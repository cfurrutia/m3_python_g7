import sys

precios = {'Notebook': 700000,
'Teclado': 25000,
'Mouse': 12000,
'Monitor': 250000,
'Escritorio': 135000,
'Tarjeta de Video': 1500000}

def imprimir(opc,lista):
    print(f'Los productos {opc}es al umbral son {lista}')

def filtro(val,opc="menor"):
    if opc=="menor":
        res = ', '.join(({k for k,v in precios.items() if v<val}))
        imprimir(opc,res)
        
    elif opc=="mayor":
        res = ', '.join(({k for k,v in precios.items() if v>val}))
        imprimir(opc,res)
    else:
        print(f'Lo sentimos, {opc} no es una operación válida')

if len(sys.argv)>2: filtro(int(sys.argv[1]),sys.argv[2])
else: filtro(int(sys.argv[1]))