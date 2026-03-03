#Ejercicio Lista 1
#Escribir una función que reciba una muestra de números en una lista y devuelva su media, con una funcion para llenar la lista

from utils import *

def media(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma / len(lista)

def llenar(lista):
    x=mayor(0)
    for i in range(x):
        lista.append(int(input("Ingrese un número: ")))

def main():
    lista = []
    llenar(lista)  
    print(media(lista))

if __name__ == "__main__":
    main()
