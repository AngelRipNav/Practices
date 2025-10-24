#Ejercicio 40: Dado tres números, determinar cuál es el del medio (ni el mayor ni el menor, el del medio del tod).

def main():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    num3 = int(input("Introduce el tercer numero: "))
    if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
        print(f"El numero del medio es: {num1}")
    elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
        print(f"El numero del medio es: {num2}")
    else:
        print(f"El numero del medio es: {num3}")
if __name__ == "__main__":
    main()