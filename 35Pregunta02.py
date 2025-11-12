#Ejercicio 58: Escriba un programa que pregunte una y otra vez si desea terminar el programa, siempre que se conteste exactamente N (en mayúsculas).

def main():
    respuesta = input("¿Desea terminar el programa?: ")
    while respuesta == "N":
        respuesta = input("¿Desea terminar el programa?: ")
    print("¡Hasta la vista!")
    


if __name__ == "__main__":
    main()
