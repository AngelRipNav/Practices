#Ejercicio 53: Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

def main():
    num=int(input("Introduce un numero entero mayor que cero: "))
    if num <= 0:
        print("¡Te he dicho un numero entero MAYOR que cero!")
    else:
        print(f"El número de divisores es: ", end="")
        for i in range(1,num+1):
            if num % i == 0:
                print(i, end=" ")
    print ()
            

if __name__ == "__main__":
    main()

