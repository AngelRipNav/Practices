#Ejercicio Lista 3
#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

from utils import *

def llenar(lista):
    x=mayor(0)
    for i in range(x):
        lista.append(int(input("Ingrese un número: ")))

def media(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma / len(lista)

def varianza(lista):
    m = media(lista)
    suma = 0
    for i in lista:
        suma = suma + (i - m) ** 2
    return suma / len(lista)

def desviacion_tipica(lista):
    return varianza(lista) ** 0.5

def estadisticas(lista):
    return {
        'media': media(lista),
        'varianza': varianza(lista),
        'desviacion': desviacion_tipica(lista)
    }

def main():
    lista = []
    llenar(lista)
    resultado = estadisticas(lista)
    print(resultado)


if __name__ == "__main__":
    main()
