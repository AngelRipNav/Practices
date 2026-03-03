#Ejercicio 02: Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def hola(nombre):
    print("¡Hola", nombre + "!")

def main():
    nom=input("Como te llamas: ")
    hola(nom)

if __name__ == "__main__":
    main()
