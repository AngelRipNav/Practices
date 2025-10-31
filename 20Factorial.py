#Ejercicio 44: Programa que me permite calcular el factorial de una serie de números acabada con la introducción del número -1.

def main():
    sw1 = False
    while not sw1:
        n=int(input("Introduce un numero entero positivo: "))
        if n != -1:
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            print(f"El factorial de {n} es {fact}")
        else:
            sw1=True


if __name__ == "__main__":
    main()
