'''
Escribe un programa para calcular el porcentaje de descuento que nos han hecho al comprar algo.

Se debe solicitar la cantidad de tarifa y lo que realmente pagamos.

Una función que pida un número > 0 y <=3000, y lo devuelva cuando sea correcto.
Una función al que le pasamos ambos precios y nos devuelve el resultado.
'''

def pedir_numero(x, y):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número ({x}-{y}): "))
        if numero > x and numero <= y:
            seguir = False
        else:
            print(f"Error: El número debe estar entre {x} y {y}.\n")
    return numero

def descuento(x, y):
    desc= x-y
    porcen=desc/x*100
    return porcen


def main():
    tarifa = pedir_numero(0,3000)
    pagado = pedir_numero(0,3000)
    calc_desc=descuento(tarifa, pagado)
    print(f"Nos han dado un {calc_desc:.2f}% de descuento!")


if __name__ == "__main__":
    main()
