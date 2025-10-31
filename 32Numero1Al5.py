#Ejercicio 32: Pedimos un número entre 1 y 5 y escribimos el número en letras.

def main():
    numero = int(input("ingrese un numero entre 1 y 5: "))
    if numero == 1:
        print("UNO")
    elif numero == 2:
        print("DOS")
    elif numero == 3:
        print("TRES")
    elif numero == 4:
        print("CUATRO")
    elif numero == 5:
        print("CINCO")
    else:
        print("ERES UN TRAMPOSO")
if __name__ == "__main__":
    main()