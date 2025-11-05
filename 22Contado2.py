#Ejercicio 45.2: Pide 2 numeros al usuario y cuenta del menor al mayor
def main():
    num1=int(input("Introduce un numero entero positivo: "))
    num2=int(input("Introduce otro numero entero positivo: "))
    if num1 < num2:
        for numerito in range(num1,num2+1):
            print(numerito, end=" ")
    else:
        for numerito in range(num2,num1+1):
            print(numerito, end=" ")
    print()

if __name__ == "__main__":
    main()
