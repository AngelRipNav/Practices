#Ejercicio Lista 4
#Escribir una función que reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

from utils import *

def calificaciones(lista):
    calificaciones=[]
    for i in range(len(lista)):
        if lista[i] >= 90:
            calificacion.append('A')
        elif lista[i] >= 80:
            calificacion.append('B')
        elif lista[i] >= 70:
            calificacion.append('C')
        elif lista[i] >= 60:
            calificacion.append('D')
        else:
            calificacion.append('F')
    return calificaciones

def llenar(lista):
    x=mayor(0)
    for i in range(x):
        lista.append(pedir_numero(0, 100))

def main():
    lista = []
    calificacion = []
    llenar(lista)
    calificacion = calificaciones(lista)
    print(calificacion)



if __name__ == "__main__":
    main()
