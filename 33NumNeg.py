#Ejercicio 55: Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

def main():

    num3=0
    num1=int(input("Cuantos valores vas a introducir: "))
    if num1 >= 0:
        for i in range (1, num1+1):
            num2=float(input(f"Introduce el número {i}: "))
            if num2 <= -1:
                num3 = num3+1
        print(f"Gracias por su colaboracion, el numero total de negativos es {num3}")
    else:
        print("¡Imposible!")



if __name__ == "__main__":
    main()
