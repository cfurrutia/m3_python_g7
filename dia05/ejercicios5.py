#  Pruebas Lógicas

nombre = "Juan"
edad = 27 # años
numero_hijos = 0
graduacion_colegio = 17 # años
duracion_uni = 6  # años
exp_laboral = 4 # años


# ¿Juan es mayor de edad?
print(edad >= 18)  # True
print(edad < 18)   # False

# ¿ Juan  se graduó del colegio antes de los 18 años ?
edad_graduacion_colegio = 17
print(edad_graduacion_colegio < 18)    # True
print(edad_graduacion_colegio == 18)   # False
print(edad_graduacion_colegio > 18)    # False
print(edad_graduacion_colegio >= 18)   # False

# ¿Juan no tiene 4 años de experiencia laboral?
print(exp_laboral != 4)  # False
print(exp_laboral == 4)  # True
print(exp_laboral < 4 or exp_laboral > 4)  # False

# ¿Juan tiene hijos?
print(numero_hijos > 0)   # False
print(numero_hijos < 1)   # True
print(numero_hijos == 1)  # False
print(numero_hijos != 1)  # True

# comparacion entre = y ==
me_llamo_juan = nombre == "Juan"  # True, estamos asiganado a me_llamo_juan el resultado de una comparacion nombre == "Juan"

""" edad > 18 y durcion_pololeo > 0

edad > 18
duracion_pololeo > 0

P = edad > 18
Q = duracion_pololeo > 0
R = 

p = T ; p = F
q = T ; q = F
r = T ; r = F

y (and) -> se deben cumplir ambas condiciones

P   O   AND
V   V    V
V   F    F
F   V    F
F   F    F

o (or) - > basta que una condicion se cumpla

P   O    OR
V   V    V
V   F    V
F   V    V
F   F    F

"""
