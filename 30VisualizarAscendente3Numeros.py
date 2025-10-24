#Ejercicio 30: Programa que lee tres números y los visualiza en orden ascendente.

def main():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    num3 = int(input("Introduce el tercer numero: "))
    if num1 <= num2 and num1 <= num3:
        if num2 <= num3:
            print(f"{num1}, {num2}, {num3}")
        else:
            print(f"{num1}, {num3}, {num2}")
    elif num2 <= num1 and num2 <= num3:
        if num1 <= num3:
            print(f"{num2}, {num1}, {num3}")
        else:
            print(f"{num2}, {num3}, {num1}")
    else:
        if num1 <= num2:
            print(f"{num3}, {num1}, {num2}")
        else:
            print(f"{num3}, {num2}, {num1}")
if __name__ == "__main__":
    main()
