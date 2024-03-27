"""
El formato de estos recordatorios son una fecha (año-mes-día), una hora y una descripción del evento.
Aplicando métodos apropiados para la estructura de datos entregada edite la lista de 
recordatorios de la siguiente manera:

1) Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar 
el Año”.

2) Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar 
de tal manera que sea el 16 de Julio.

3) Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día 
del trabajo.

4) Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a 
las 22 hrs.
"""

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                ['2021-05-01', "15:00", "No trabajar"],
                ['2021-07-15', "13:00", "No hacer nada es feriado"],
                ['2021-09-18', "16:00", "Ramadas"],
                ['2021-12-25', "00:00", "Navidad"]]

# Agregar el evento de Empezar el año
recordatorios.append(['2021-02-02', '06:00', 'Empezar el Año']) 

# Modificar evento para el dia feriado
recordatorios[2][0] = '2021-07-16'

# Eliminar evento del dia del trabajo
del recordatorios[1]

# Agregar el evento de Cena de navidad y Cena de Año Nuevo
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Muestra lista recordatorio modificada y ordenada

# recordatorios.sort()
# print(recordatorios)

print(sorted(recordatorios)) 
