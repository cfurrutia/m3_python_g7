""" 
Crear un archivo conversiones.py y una estructura de datos apropiada que permita 
ingresar tasas de conversión. Las distintas tasas de conversión se deben ingresar 
mediante sys.argv 

los valores que vamos a buscar :
Sol peruano: 0.0046
Peso Argentino: 0.093
Dólar Americano: 0.00013
"""
import sys

# ingreso de datos de conversion en el siguiente orden: Sol, Peso Argentino, Dólar Americano. 
tasas_de_conversion = { 'Sol': float(sys.argv[1]),                         
                    'Peso Argentino': float(sys.argv[2]),                 
                    'Dolar Americano': float(sys.argv[3]),                 
}
# ingreso el valor para convertir en pesos Chilenos
pesos_chilenos = int(sys.argv[4])

# Calcula la cantidad multiplicando la cantidad de pesos chilenos por la tasa de conversion.
equivalencia = { 'Soles': pesos_chilenos * tasas_de_conversion['Sol'],                     
            'Pesos Argentinos': pesos_chilenos * tasas_de_conversion['Peso Argentino'],   
            'Dolares': pesos_chilenos * tasas_de_conversion['Dolar Americano']
}
# Imprime un mensaje indicando la cantidad para convertir
print(f"Los {pesos_chilenos} Pesos equivalen a: ")

# Imprime la cantidad  equivalente a pesos chilenos.
print(f"{equivalencia['Soles']} Soles")
print(f"{equivalencia['Pesos Argentinos']} Pesos Argentinos")
print(f"{equivalencia['Dolares']} Dolares")
