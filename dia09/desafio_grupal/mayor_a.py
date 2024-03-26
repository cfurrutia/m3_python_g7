"""
Actividad 1 - Filtrado compacto
Se solicita devolver un informe resumido que exponga los meses que superan un cierto 
umbral. El programa debe retornar un diccionario con el mes y el valor asociado 
siempre y cuando superen el umbral especificado. 
Ejemplo:
python mayor_a.py 40000   -->   {'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000}

integrantes

Carlos Urrutia curiqueo
Manuel Ruiz Uribe
Yessenia Millar  Reyes

"""
import sys

# umbral mensual
umbral = int(sys.argv[1])

# lista de ventas
ventas = {"Enero": 15000,"Febrero": 22000,"Marzo": 12000,"Abril": 17000,"Mayo": 81000,"Junio": 13000,
        "Julio": 21000,"Agosto": 41200,"Septiembre": 25000,"Octubre": 21500,"Noviembre": 91000,"Diciembre": 21000,}

"""
ventas_sobreUmbral = {}  # lista vacia

for mes, valor in ventas.items():
        if valor > umbral:
                ventas_sobreUmbral[mes] = valor # recorrido
print(ventas_sobreUmbral)  # entrega lista 
"""

# Busqueda de ventas mensual segun el umbral del valor        
print({mes: valor for mes, valor in ventas.items() if valor>umbral})

