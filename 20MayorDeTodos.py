#Programar cual es el mayor de los 3 numeros que hay que pedir

def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num3 = float(input("Introduce el tercer numero: "))
    if (num1 > num2 and num1 > num3):
        print(f"El primer numero ({num1}) es el mayor")
    elif (num2 > num1 and num2 > num3):
        print(f"El segundo numero ({num2}) es el mayor")
    else:
        print(f"El tercer numero ({num3}) es el mayor")

if __name__ == "__main__":
    main()