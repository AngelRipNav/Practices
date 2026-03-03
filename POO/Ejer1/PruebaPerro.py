from Perro import *

def main():
    mi_perro = Perro("Nana", "Yorsay")
    otroPerro = Perro("Rambo")
    print()
    print(mi_perro.nombre)
    print(Perro.especie)
    print(mi_perro.raza)
    mi_perro.ladrar()
    mi_perro.camina(10)
    print()
    print(mi_perro.nombre)
    print(Perro.especie)
    print(mi_perro.raza)
    for i in range(1,11):
        print("Guau", end=" ")
    print()
    mi_perro.camina(100)
if __name__ == "__main__":
    main()
