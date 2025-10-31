#Ejercicio 11: Comprueba si hay un 10 o no

def main():
    sw1=False
    nota = int(input("Introduce una nota: "))
    while nota < -1  or nota > 10:    
        print("Tu nota es incorrecta")
        nota = int(input("Introduce una nota: "))

    while nota != -1:
        if nota == 10:
                sw1=True

#Bucle para obligar a que la nota este dentro del rango adecuado.                                                                           
        nota = int(input("Introduce una nota: "))
        while nota < -1  or nota > 10:    
            print("Tu nota es incorrecta")
            nota = int(input("Introduce una nota: "))


    if sw1==True:
        print("Hay al menos un 10")
    else:
        print("No hay NINGUN 10")


if __name__ == "__main__":
    main()
