#Ejercicio 49: Programa que permite realizar una cuenta atras, desde el numero que introduzca el usuario hasta cero. Lo realizará de dos formas distintas. (Con For y luego con Why)

def main():
    num=int(input("Introduce un numero entero positivo "))
    while num != -1:
        print(num, end=" ")
        num = num -1
    print()

if __name__ == "__main__":
    main()
