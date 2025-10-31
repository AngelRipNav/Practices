#Ejercicio 38: Dado un número y guardado en una variable, el usuario debe adivinar el número almacenado, el ordenador nos irá diciendo si es mayor, menor o igual.

def main():

    num = int(input("Introduce un numero: "))

    adiv = 5
    while num != adiv:
        if num < adiv:
            print(f"Tu numero es menor al numero que tienes que adivinar")
        else:
            print(f"Tu numero es mayor al numero que tienes que adivinar")

        num = int(input("Introduce un numero: "))
    
    print(f"Tu numero es igual al numero que tienes que adivinar")





if __name__ == "__main__":
    main()
