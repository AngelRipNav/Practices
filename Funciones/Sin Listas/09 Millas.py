'''
Programa que dado un valor en millas nos lo traduce a metros.

El programa debe tener:

Una función que pida un número > 0  y lo devuelva cuando sea correcto
Una función que reciba como argumento una cantidad (en millas) y nos devuelva la cantidad en metros.
'''

def pedir_numero(x):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número (superior a {x}): "))
        if numero > x:
            seguir = False
        else:
            print(f"Error: El número debe superior a {x}.\n")
    return numero

def millas(numero):
    metros = numero * 1609.344
    return metros

def main():
    numero = pedir_numero(0)
    metros = millas(numero)
    print(f"{numero} millas son {metros:.2f} metros.")


if __name__ == "__main__":
    main()
