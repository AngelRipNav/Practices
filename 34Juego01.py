#Ejercicio 34: Juego dados aleatorios, el numero mas grande gana, si hay empate se declara empate.

def main():
    import random
    alvaro = random.randrange(1, 7)
    barbara = random.randrange(1, 7)
    print("JUEGO DE DADOS(1)")
    print(f"Alvaro ha sacado un {alvaro}")
    print(f"Barbara ha sacado un {barbara}")
    if alvaro > barbara:
        print("Gana Alvaro")
    elif barbara > alvaro:
        print("Gana Barbara")
    else:
        print("Empate")

if __name__ == "__main__":
    main()