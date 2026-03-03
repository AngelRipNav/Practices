from Libro import *
from utils_v2 import *

def main():
    pre1 =pedir_float(0, 999, "Introduce un precio") 
    tot1 = int(input("Numero total de libros: ")) 
    prest1 =pedir_Num_Premium(0, tot1, "Numero total de libros prestados: ")
    
    libro1=Libro("Piratas del Caribe", "Jack Sparrow", "Pirineus", 2015, 44, pre1, tot1, prest1)
    

    libro2=Libro("Barbie: Un mundo de Fantasia", "Barbie", "Carspesky", 2017, 45)

    libro3=Libro("La flor de la muerte rosa", "Bluedier", "ManHatan")

    print(libro1.mostrarLibro())
    print(libro2.mostrarLibro())
    print(libro3.mostrarLibro())

    while confirmar("Quieres prestar un libro"):
        if confirmar("Quieres prestar el libro 1"):
            if libro1.prestarLibro():
                print("Prestado el libro ", libro1.get_titulo())
            else:
                print("No quedan ejemplares de ", libro1.get_titulo())
        elif confirmar("Quieres prestar el libro 2"):
            if libro2.prestarLibro():
                print("Prestado el libro ", libro2.get_titulo())
            else:
                print("No quedan ejemplares de ", libro2.get_titulo())
        elif confirmar("Quieres prestar el libro 3"):
            if libro3.prestarLibro():
                print("Prestado el libro ", libro3.get_titulo())
            else:
                print("No quedan ejemplares de ", libro3.get_titulo())
    
    while confirmar("Quieres devolver un libro"):
        if confirmar("Quieres devolver el libro 1"):
            if libro1.devolverLibro():
                print("Devuelto el libro ", libro1.get_titulo())
            else:
                print("No hay ejemplares de ", libro1.get_titulo())
        elif confirmar("Quieres devolver el libro 2"):
            if libro2.devolverLibro():
                print("Devuelto el libro ", libro2.get_titulo())
            else:
                print("No hay ejemplares de ", libro2.get_titulo())
        elif confirmar("Quieres devolver el libro 3"):
            if libro3.devolverLibro():
                print("Devuelto el libro ", libro3.get_titulo())
            else:
                print("No hay ejemplares de ", libro3.get_titulo())
        
'''    for i in range (2):
        centrar_titulo("Prestar")
        if libro1.prestarLibro():
            print("Prestado el libro ", libro1.get_titulo())
        else:
            print("No quedan ejemplares de ", libro1.get_titulo())
        print()
 
    print(libro1.mostrarLibro())
    for i in range (4):
        centrar_titulo("Devolver")
        if libro1.devolverLibro():
            print("Devuelto el libro ", libro1.get_titulo())
        else:
            print("No hay ejemplares de ", libro1.get_titulo())
        print()
    print(libro1.mostrarLibro())'''




if __name__ == "__main__":
    main()
