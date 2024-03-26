""" 
Supongamos que queremos mostrar una tabla de multiplicar, por ejemplo la tabla 
del 5. Esto se puede escribir como:
"""

"""
for numero in range(10):   # 0 al 9
    print(f"5 * {numero} = {5 * numero}")
"""

"""    
for numero in range(1,11):   # 1 al 10
    print(f"5 * {numero} = {5 * numero}")
"""
    
for tabla in range(1,11):#1-10
    print(f" tabla del numero {tabla}\n")
    
    for  numero in range(1,11):#1-10
        print(f"{tabla} * {numero} = {tabla * numero}")
        
        
        