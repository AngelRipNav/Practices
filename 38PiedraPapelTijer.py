#Ejercicio 38: Crea un juego de piedra papel y tijera de manera aleatoria.

def main():
    import random
    pptj=random.randrange(1,4)
    if pptj==1:
        print("Juan ha sacado Piedra")
    elif pptj==2:
        print("Juan ha sacado Papel")
    else:
        print("Juan ha sacado Tijera")


    ppti=random.randrange(1,4)
    if ppti==1:
        print("Ines ha sacado Piedra")
    elif ppti==2:
        print("Ines ha sacado Papel")
    else:
        print("Ines ha sacado Tijera")

    print("RESULTADO:")

    if pptj==ppti:
        print("Empataron...")
    elif (pptj==1 and ppti==3) or (pptj==2 and ppti==1) or (pptj==3 and ppti==2):
        print("HA GANADO JUAN")
    else:
        print("HA GANADO INES")

if __name__ == "__main__":
    main()