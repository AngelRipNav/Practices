'''
Escribe un programa que pida un año y que escriba si es bisiesto o no.

Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.

COMPROBADOR DE AÑOS BISIESTOS
Escribe un año y le diré si es bisiesto: 2000
El año 2000 es un año bisiesto.

Una función que pida un número > 0 y <=4999, y lo devuelva cuando sea correcto.
Una función que devuelva True si es bisiesto y False si no lo es.
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

def bisiesto(numero):
    bis = "no"
    if numero % 4 == 0 and (numero % 100 != 0 or numero % 400 == 0):
        bis  = "si"
    return bis

def main():
    numero = pedir_numero(0,4999)
    if bisiesto(numero) == "si":
        print(f"El año {numero} es un año bisiesto.")
    else:
        print(f"El año {numero} es un año NO bisiesto.")


if __name__ == "__main__":
    main()
