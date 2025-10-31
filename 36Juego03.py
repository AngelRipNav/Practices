#Ejercicio 36: Juego dados aleatorios, el numero mas grande gana, si hay empate se decide con el otro dado, si siguen empatados se declara empate.

def main():
    import random
    Fernando = random.randrange(1, 7)
    Elena = random.randrange(1, 7)
    Fernando2 = random.randrange(1, 7)
    Elena2 = random.randrange(1, 7)
    print("JUEGO DE DADOS(3)")
    print(f"Fernando ha sacado un {Fernando} y un {Fernando2}")
    print(f"Elena ha sacado un {Elena} y un {Elena2}")
    if Fernando > Elena:
        print("Gana Fernando")
    elif Elena> Fernando:
        print("Gana Elena")
    else:
        if Fernando2 > Elena2:
            print("Gana Fernando")
        elif Elena2 > Fernando2:
            print("Gana Elena")
        else:
            print("Empate")
if __name__ == "__main__":
    main()