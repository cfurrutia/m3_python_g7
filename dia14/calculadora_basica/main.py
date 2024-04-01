import suma
import os
import sys
import time
import resta as r
from input import captura_datos
clear = "cls" if sys.platform == "win32" else "clear"

opcion = input("""Esto es una calculadora: 
¿Qué operación le gustaría realizar?
1. Sumar
2. Restar
0. Salir
> """)
time.sleep(2)
os.system(clear)

if opcion == '1':
    x, y = captura_datos() # 3ra forma de importar
    suma.sumar(x,y) # 1era forma de importar
elif opcion == '2':
    x, y = captura_datos() # 3ra forma de importar
    r.restar(x,y) # 2da forma de importar
elif opcion == '0':
    print('Nos vemos a la próxima')
else:
    # exit()
    print('No existe esta Operación')
