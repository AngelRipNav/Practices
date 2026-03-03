'''
Escribe un programa que tenga:

Una función que pida un número > 0 y <=20 para solicitar la anchura
Una función que lo dibuje con caracteres producto (*):
Anchura del triángulo: 4
*
* *
* * *
* * * *
* * *
* *
*
'''

def pedir_anchura(x, y):

    seguir = True
    while seguir:
        anchura = int(input("Anchura del triángulo: "))
        if anchura > x and anchura <= y:
            seguir = False
        else:
            print(f"\nError: El valor debe estar entre {x} y {y}.\n")
    return anchura

def dibujar_triangulo(ancho):

    for i in range(1, ancho + 1):
        for j in range(i):
            print("*", end=" ")
        print()
    

    for i in range(ancho - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    anchura = pedir_anchura(0,20)
    dibujar_triangulo(anchura)


if __name__ == "__main__":
    main()
