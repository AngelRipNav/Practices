#Ejercicio 28: Programa que lee dos números positivos y distintos y nos dice si el menor es divisor del mayor.

def main():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    if num1 < num2:
        menor = num1
        mayor = num2
    else:
        menor = num2
        mayor = num1
    if mayor % menor == 0:
        print(f"{menor} es divisor de {mayor}")
    else:
        print(f"{menor} no es divisor de {mayor}")

if __name__ == "__main__":
    main()