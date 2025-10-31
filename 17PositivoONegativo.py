#Actividad 17 Un programa que lee un numero y dice si es positivo o negativo (el cero es positivo)

def main():
    num = int(input("Introduce un numero: "))
    if num >= 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")

if __name__ == "__main__":
    main()