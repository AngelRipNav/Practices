#Ejercicio 03.2: Cuarto bucle empezando de 1 al 200 mostrando solo los pares y no va de 2 en 2

def main():
    for i in range(2,201):
        if i % 2 == 0:
            print(f"{i}", end=" ")
    print()
if __name__ == "__main__":
    main()