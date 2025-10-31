#Ejercicio 31: Programa que lee un número entre 1 y 12 y muestra el mes correspondiente.

def main():
    numero = int (input("Ingresa un número entre 1 y 12: "))
    if numero == 1:
        print("Enero")
    elif numero == 2:
        print("Febrero")
    elif numero == 3:
        print("Marzo")
    elif numero == 4:
        print("Abril")
    elif numero == 5:
        print("Mayo")
    elif numero == 6:
        print("Junio")
    elif numero == 7:
        print("Julio")
    elif numero == 8:
        print("Agosto")
    elif numero == 9:
        print("Setiembre")
    elif numero == 10:
        print("Octubre")
    elif numero == 11:
        print("Noviembre")
    elif numero == 12:
        print("Diciembre")
    else:
        print("NO EXISTE ESE MES")

if __name__ == "__main__":
    main()