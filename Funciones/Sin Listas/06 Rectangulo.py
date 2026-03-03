'''
Escribe un programa que tenga:

Una función que pida un número > 0 y <=20, utilízala tanto para en ancho como para la altura
 Una función que dibuje el rectángulo con caracteres producto (*):
Anchura del rectángulo: 5
Altura del rectángulo: 3
* * * * *
* * * * *
* * * * *

Ampliación:

Escriba un programa que pida la anchura y altura de un rectángulo y el carácter a utilizar en el dibujo:

Anchura del rectángulo: 5
Altura del rectángulo: 3
Carácter a utilizar: o
o o o o o
o o o o o
o o o o o

Nota: El carácter a utilizar en el dibujo se puede enviar a la función como tercer argumento.
'''

import math

def rango(x, y):
    seguir = True
    while seguir:
        valor = int(input("Introduce un número (Primero Altura, luego Ancho): "))
        if valor >= x and valor <= y:
            seguir = False
        else:
            print(f"Error: El valor debe estar entre {x} y {y}.\n")
    return valor

def main():
    altura = rango(0,200)
    ancho = rango(0,200)
    
    for i in range(altura):
        for j in range(ancho):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
