#Ejercicio 51: El usuario "piensa" un número del 1 al 100 y el ordenador lo adivina. (el usuario debe indicarle al ordenador si es mayor, menor o igual):

def main():
    num = int(input("Introduce un numero: "))

    adiv = 0

    menor = 1
    mayor = 100
    adiv = 0

    while adiv != num:
        adiv = (menor + mayor) // 2
        print(f"El ordenador adivina: {adiv}")
        mmi = input("Dime si es mayor, menor o igual: ")
        if mmi=="mayor":
            menor = adiv + 1
        elif mmi=="menor":
            mayor = adiv - 1
        else:
            print("Perfecto!")
    print("Celebrame he adivinado")

if __name__ == "__main__":
    main()
