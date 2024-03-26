"""
Actividad 2 - Primeros auxilios
Se requiere la construcción de una aplicación interactiva  que 
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega 
en tiempo real. 

integrantes

Carlos Urrutia curiqueo
Manuel Ruiz Uribe
Yessenia Millar  Reyes

"""

# Paso 1.- ¿paciente responde a estimulos?
estimulos = input("¿ Paciente Responde a Estimulos? favor responder si o no \n")  

# validacion respuesta de entrada
while estimulos.lower() != "si" and estimulos.lower() != "no":
    print("Respuesta no válida! favor responder si o no \n")  
    estimulos = input("¿ Paciente Responde a Estimulos? favor responder si o no\n")

if estimulos.lower() == "si":
        print("Verificar la necesidad de llevarlo al hospital más cercano\n")
            
else:
    print("Abrir la via aerea \n")
        
    #  Paso 2 .- respiración del paciente
    respirar = input("¿El paciente respira?  favor responder si o no \n")   
        
    while respirar.lower() != "si" and respirar.lower() != "no": 
        print("Respuesta no válida! favor responder si o no \n") 
        respirar = input("¿El paciente respira?  favor responder si o no \n")
            
    if respirar.lower() == "si":
        print("Permitir posicion de suficiente ventilación\n")   
            
    else:
        print("Administrar 5 ventilaciones y llamar a Ambulancia \n")
        
        # se añade llegada de la ambulancia
        ambulancia = input("¿Llegó la ambulancia?  favor responder si o no \n").lower()
        
        while ambulancia == 'no':
            signos_vitales = input("¿El paciente tiene signos de vida? favor responder si o no \n")  
            while signos_vitales.lower() != "si" and signos_vitales.lower() != "no":
                print("Respuesta no válida! favor responder si o no \n") 
                signos_vitales = input("¿El paciente tiene signos de vida? favor responder si o no \n") 
            
            if signos_vitales.lower() == "si":
                print("Reevaluar a la espera de la Ambulancia\n")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia\n")    

            ambulancia = input("¿Llegó la ambulancia?  favor responder si o no \n").lower() 
        

print("FIN DE LA EMERGENCIA")   