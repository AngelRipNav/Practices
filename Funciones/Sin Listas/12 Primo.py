'''
Programa que debe ir pidiendo números al usuario hasta que el usuario introduzca el cero. Para cada numero introducido, hay que decir si es primo o no.

Hay que recordar que:

un numero es primo, si solo es divisible por si mismo y por 1.
El 1 no es primo por convenio.
El programa debe tener una función que permita saber si un número (que se le pasará como parámetro) es primo o no.
'''

def primo(num):
    primo = True
    i=2

    while (i != num and primo==True):
        if num % i != 0:
            i=i+1
        else:
            primo = False

    return primo


def pedir_numero():
    seguir = True
    while seguir:
        numero = int(input("\nIntroduce un número (0 para finalizar): "))
        if numero == 0:
            seguir = False

        elif numero == 1:
            print("El número 1 no es primo")
        else:
            if primo(numero):
                print(f"El número {numero} es primo")
            else:
                print(f"El número {numero} no es primo")

def main():
    print("Programa para verificar si los números son primos")
    print("=" * 49)
    pedir_numero()
    print("\n¡Programa finalizado!")


if __name__ == "__main__":
    main()
