precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}

def filtrar(precios, umbral):
    filtro = {k:v for k,v in precios.items() if v > umbral}
    return filtro

filtrar(precios, 12000)
