#Ejercicio 57: Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).

def main():
    respuesta = input("¿Desea continuar con el programa? (sí/no): ")
    while respuesta == "sí":
        respuesta = input("¿Desea continuar con el programa? (sí/no): ")
    print("¡Hasta la vista!")
    


if __name__ == "__main__":
    main()
