#Ejercicio 41: Algoritmo que lee una secuencia de números no nulos, terminada con la introducción de un 0, y obtiene e imprime si ha leído algún número negativo, cuantos positivos y cuantos negativos. utilizando un bucle until

def main():
    bucle=False
    negativo=False
    neg=0
    pos=0
    while not bucle:
        num = int(input("Introduce un numero: "))
        if num != 0:
            if num < 0:
                neg = neg + 1
                negativo = True
            else:
                pos = pos + 1
        else:
            bucle = True
    if negativo:
        print("Se ha introducido AL MENOS 1 numero negativo!")
    print(f"Se han introducido {pos} numeros positivos")
    print(f"Se han introducido {neg} numeros negativos")


if __name__ == "__main__":
    main()
