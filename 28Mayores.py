#Ejercicio 50:Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

def main():
    num1=int(input("Cuantos valores vas a introducir: "))
    if num1 >= 1:
        num2=int(input("Introduce un numero: "))
        for i in range (1, num1):
            num3=int(input(f"Introduce un numero más grande que {num2}: "))
            if num2 >= num3:
                print("Esto no es un numero mayor!")
            else:
                num2=num3
        print("Gracias por su colaboracion")
    else:
        print("¡Imposible!")
if __name__ == "__main__":
    main()
