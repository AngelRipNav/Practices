#Ejercicio 59: Escriba un programa que pida números enteros mientras sean cada vez más grandes.

def main():
    
    mayor= True
    num2=int(input("Introduce un numero: "))
    while mayor:
        num3=int(input(f"Introduce un numero más grande que {num2}: "))
        if num2 >= num3:
            print(f"{num3} no es mayor que {num2}")
            mayor=False
        else:
            num2=num3
            


if __name__ == "__main__":
    main()
