#Ejercicio 03: Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n):
    if n == 0:
        n=1
    else:
        n= n * factorial(n-1)
    return n

def main():
    num = int(input("Introduce un número entero positivo: "))
    while num < 0:
        print('\nNO SE PUEDE RESOLVER VUELVE A INTRODUCIRLO\n')
        num = int(input("Introduce un número entero positivo: "))
    fact = factorial(num)
    print("\nEl factorial es", fact)

if __name__ == "__main__":
    main()
