#Ejercicio 45.3: Pide 2 numeros al usuario y cuenta del menor al mayor

def main():
    num1 = int(input("Introduce un numero entero positivo: "))
    num2 = int(input("Introduce otro numero entero positivo: "))
    
    if num1 < num2:
        inicio = num1
        final = num2
    else:
        inicio = num2
        final = num1
        
    for numerito in range(inicio, final + 1):
        print(numerito, end=" ")
    print()

if __name__ == "__main__":
    main()
