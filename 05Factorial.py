#Ejercicio 05: Calculo del factorial de un numero N introducido por teclado

def main():
    n=int(input("Introduce un numero entero positivo: "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"El factorial de {n} es {fact}")

if __name__ == "__main__":
    main()