#Ejercicio 54: Escriba un programa que pregunte cuantos números se van a introducir, pida esos números (que puedan ser decimales) y calcule su suma.

def main():
    num3=0
    num1=int(input("Cuantos valores vas a introducir: "))
    if num1 >= 1:
        for i in range (1, num1+1):
            num2=float(input(f"Introduce el número {i}: "))
            num3 = num3 + num2
        print(f"Gracias por su colaboracion, la suma total es de {num3}")
    else:
        print("¡Imposible!")
if __name__ == "__main__":
    main()
