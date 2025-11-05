#Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y escriba el mayor, el menor y la media aritmética.

#Se recuerda que la media aritmética de un conjunto de valores es la suma de esos valores dividida por la cantidad de valores.

def main():

    num3=99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    num4=0
    num5=0

    num1=int(input("Cuantos valores vas a introducir: "))
    if num1 >= 0:
        for i in range (1, num1+1):
            num2=int(input(f"Introduce el número {i}: "))
            if num2 > num4:
                num4 = num2
            if num2 < num3:
                num3 = num2
            num5 = num5 + num2
            media = num5 / num1

        print(f"Gracias por su colaboracion, el numero menor es {num3}, el mayor es {num4} y la media es {media}")
    else:
        print("¡Imposible!")




if __name__ == "__main__":
    main()
