estimulos = input("¿Responde a estimulos? [s/n]").lower()

if estimulos ==  "s":
    #respuesta ="respuetas si"
    print("Valorar la necesidad de llevarlo al hospital mas cerno")
else:
    print("Abrir la via Aérea")
    respira = input("¿Respira? [s/n]").lower()

    if respira == "s":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a Ambulancia")

        signos = input("¿Tiene signos de vida? [s/n]").lower()
        if signos == "s":
                print("Reevaluar a la espera de la ambulancia")
        else:
            print("Administrar compresiones torácicas hasta que llegue la ambulancia")

        ambulancia = input("¿Llegó la ambulancia? [s/n]").lower()#"n"#inicialmente no esta la ambulancia

        while ambulancia == 'n':
            signos = input("¿Tiene signos de vida? [s/n]").lower()

            if signos == "s":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")

            ambulancia = input("¿Llegó la ambulancia? [s/n]").lower()   

print("Sistema de primeros auxilios terminado")    
