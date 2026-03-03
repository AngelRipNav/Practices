'''Crea un proyecto nuevo, llamalo Figuras (donde estará el main()), y crea un fichero nuevo dentro del proyecto, en el mismo pakage,  para cada una de las siguientes clases:

Crea una clase Rectangulo.

Como atributos miembro tendremos la longitud de la sus lados, base y altura.
Como métodos miembro:
perimetro() nos  devuelve el perímetro del rectángulo.
area() nos devuelve el área del rectángulo.
Crea una clase Cuadrado.

Como atributo miembro tendremos la longitud de su lado.
Como métodos miembro:
perimetro() nos  devuelve el perímetro del cuadrado.
area() nos devuelve el área del cuadrado.
Crea una clase TrianguloEquilatero.

Como atributos miembro tendremos la longitud de su base y su altura.
Como métodos miembro:
perimetro() nos  devuelve el perímetro del triángulo.
area() nos devuelve el área del triángulo.
Crea una clase Circulo.

Como atributo miembro tendremos la longitud de su radio.
Como métodos miembro:
perimetro() nos  devuelve el perímetro del círculo.
area() nos devuelve el área del círculo.
En el programa principal:

Haz un menú para que el usuario pueda elegir la figura a trabajar. Este menú debe repetirse hasta que el usuario decida pulsar la opción de salir.
Los opciones del menú serán:
Cuadrado
Rectángulo
Triángulo equilátero
Círculo
Salir
Para cada una de las opciones se debe pedir los datos necesarios, instanciar el objeto correspondiente y mostrar su perímetro y su área.'''

from Figuras import *
from utils_v2 import *

def main():
    seguir = True        
    while seguir:
        menu = ["1. Cuadrado",
            "2. Rectángulo",
            "3. Triángulo equilátero",
            "4. Círculo",
            "5. Salir"]
        centrar_titulo("GESTIÓN DE PROYECTOS")
        mostrarMenu(menu)
        op = pedir_num_extra(1, 5, "\nSelecciona una opcion")
        if op ==1:
            base=mayor_premium("Escribe la base del cuadrado", 0)
            altura=mayor_premium( "Escribe la altura del cuadrado", 0)
            cuadrado1=Cuadrado(base, altura)
            print(f"El cuadrado tiene un perimetro de {cuadrado1.perimetro()}")
            print(f"El cuadrado tiene un area de {cuadrado1.area()}")
        if op ==2:
            base=mayor_premium("Escribe la base del rectangulo", 0)
            altura=mayor_premium( "Escribe la altura del rectangulo", 0)
            rectangulo1=Rectangulo(base, altura)
            print(f"El rectangulo tiene un perimetro de {rectangulo1.perimetro()}")
            print(f"El rectangulo tiene un area de {rectangulo1.area()}")
        if op ==3:
            base=mayor_premium("Escribe la base del triangulo", 0)
            altura=mayor_premium( "Escribe la altura del triangulo", 0)
            triangulo1=TrianguloEquilatero(base, altura)
            print(f"El triangulo tiene un perimetro de {triangulo1.perimetro()}")
            print(f"El triangulo tiene un area de {triangulo1.area()}")
        if op ==4:
            radio=mayor_premium( "Escribe el radio del circulo", 0)
            circulo1=Circulo(radio)
            print(f"El circulo tiene un perimetro de {circulo1.perimetro()}")
            print(f"El circulo tiene un area de {circulo1.area()}")
        if op ==5:
            sigo = confirmar("Esta seguro que quiere salir")
            if sigo:
                seguir = False
if __name__ == "__main__":
    main()
