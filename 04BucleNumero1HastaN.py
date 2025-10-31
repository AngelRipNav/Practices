#Ejercicio 04: Bucle que pide un número N e imprime los números del 1 al N

def main():
    n=int(input("Introduce un numero entero positivo: "))
    for i in range(1,n+1):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()