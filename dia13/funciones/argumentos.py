def f(*args):
    return args

def funcion_tuplas(*parametros):
    print(parametros)
    return parametros

output = funcion_tuplas(1,[2,3],'hola',{'clave':[4]})
print(type(output))

def funcion_diccionario(**kwargs):

    return kwargs

output = funcion_diccionario(valor = 1, texto = 'hola', lista_nombres = [4,5,6,7])
print(type(output))
