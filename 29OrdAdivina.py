#Ejercicio 51: Programa que lee un numero entero y positivo y nos indica si es primo o no.

def main():
    num = int(input("Introduce un numero entero positivo: "))
    primo = True
    i=2
    while (i != num and primo==True):
        if num % i != 0:
            i=i+1
        else:
            primo = False

    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")


if __name__ == "__main__":
    main()
