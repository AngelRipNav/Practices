#Programar un comprobador de 2 numeros que nos dice cual es el mayor, menor o iguales

def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    if num1 < num2:
        print(f"El numero {num1} es menor que {num2}")
    elif num1 == num2:
        print(f"El numero {num1} es igual que {num2}")
    else:
        print(f"El numero {num1} es mayor que {num2}")

if __name__ == "__main__":
    main()