#Ejercicio 23: Programa que lee un año y nos dice si es bisiesto o no.

def main():
    año = int(input("Introduce el año: "))
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print(f"El año {año} es bisiesto")
            else:
                print(f"El año {año} no es bisiesto")
        else:
            print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
if __name__ == "__main__":
    main()