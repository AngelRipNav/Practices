#Ejercicio 01: Alternativa QUE TE DICE SOLO SI ERES MAYOR DE EDAD O MENOR

def main():
    edad = int(input("Ingrese su edad: "))
    
    if edad >= 18:
        print("ERES MAYOR DE EDAD")

    else:
        print("ERES MENOR DE EDAD")

if __name__ == "__main__":
    main()