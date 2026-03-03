#Funcion que comprueba que las respuestas sean si o no
def si_no(m):
    bucle = True
    while bucle:
        respuesta = input(m).strip().lower()
        if respuesta == "si" or respuesta == "no":
            bucle=False
        else:
            print("\nError: La respuesta tiene que ser si o no\n")
    return respuesta

def pedir_numero(x, y):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número entre {x} y {y}: "))
        if numero >= x and numero <= y:
            seguir = False
        else:
            print(f"Error: El número debe estar entre {x} y {y}.\n")
    return numero

def mayor(x):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número (superior a {x}): "))
        if numero > x:
            seguir = False
        else:
            print(f"Error: El número debe superior a {x}.\n")
    return numero


def pedir_precio(x, y):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un precio entre {x} y {y}: "))
        if numero > x and numero <= y:
            seguir = False
        else:
            print(f"Error: El precio debe estar entre {x} y {y}.\n")
    return numero


def pedir_num_extra(x, y, z):
    seguir = True
    while seguir:
        numero = int(input(f"{z} entre {x} y {y}: "))
        if numero >= x and numero <= y:
            seguir = False
        else:
            print(f"El número debe estar entre {x} y {y}.\n")
    return numero


def main():
    print()


if __name__ == "__main__":
    main()
