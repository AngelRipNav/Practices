#Ejercicio Lista 2
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

from utils import *

def cuadrados(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2
    return lista

def llenar(lista):
    x=mayor(0)
    for i in range(x):
        lista.append(int(input("Ingrese un número: ")))

def main():
    lista = []
    llenar(lista)
    print(cuadrados(lista))


if __name__ == "__main__":
    main()
