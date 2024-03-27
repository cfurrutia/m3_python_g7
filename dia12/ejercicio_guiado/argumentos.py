import sys

nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]

print(f"Mi nombre es {nombre}")                                 # Mi nombre es Carlos
print(f"Mi apellido es {apellido}")                             # Mi apellido es Urrutia
print(f"Mi edad es {edad}")                                     # Mi edad es 36
print(f"El nombre del archivo es {sys.argv[0]}")                # El nombre del archivo es argumentos.py

print(type(sys.argv))                                           # <class 'list'>


