#Ejercicio 42: Algoritmo que lee una secuencia de notas (con valores que van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.

def main():
    sw1=False
    nota=int(input("Introduce una nota del 0 al 10 (-1 para terminar): "))
    while nota != -1:
        if nota == 10:
            sw1=True
        nota=int(input("Introduce una nota del 0 al 10 (-1 para terminar): "))
    if sw1:
        print("HUBO AL MENOS UN 10")
    else:
        print("NO HUBO NINGUN 10")

if __name__ == "__main__":
    main()
