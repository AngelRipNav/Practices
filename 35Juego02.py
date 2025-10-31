#Ejercicio 35: Juego dados aleatorios, numero total mas  grande gana, si hay empate gana el que tenga el dado mas alto, si siguen empatados, se declara empate.

def main():
    import random
    elena = random.randrange(1, 7)
    fernando = random.randrange(1, 7)
    elena2 = random.randrange(1, 7)
    fernando2 = random.randrange(1, 7)
    print("JUEGO DE DADOS(2)")
    print(f"Carmen ha sacado un {elena} y un {elena2}")
    print(f"David ha sacado un {fernando} y un {fernando2}")
    if elena + elena2 > fernando + fernando2:
        print("Gana Carmen")
    elif fernando + fernando2 > elena +elena2:
        print("Gana David")
    else:
        if (elena2 > fernando2) or (elena > fernando):
            print("Gana Carmen")
        elif (fernando2 > elena2) or (fernando > elena):
            print("Gana David")
        else:
            print("Empate")

if __name__ == "__main__":
    main()