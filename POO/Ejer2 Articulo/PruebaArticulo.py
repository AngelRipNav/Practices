from Articulo import *
from utils_v2 import *

def main():
    articulo1=Articulo(35, "Piratas del Caribe", "Blue Ray", 15)
    articulo2=Articulo(36, "Barbie: Un mundo de Fantasia", "DVD", 7.5)

    centrar_titulo("Articulo 1")
    articulo1.mostrarArticulo()

    centrar_titulo("Articulo 2")
    articulo2.mostrarArticulo()

if __name__ == "__main__":
    main()
