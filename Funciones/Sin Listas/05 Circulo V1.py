#Ejercicio 05: Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math

def mayor():
    x=False
    print('\nNO SE PUEDE RESOLVER VUELVE A INTRODUCIRLO\n')
    while not x:
        n=int(input("Introduce un número entero positivo: "))
        if n < 0: 
            print('\nNO SE PUEDE RESOLVER VUELVE A INTRODUCIRLO\n')
        else:
            x=True
    return n

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

def main():
    radio = float(input("Introduce el radio del círculo: "))
    if radio < 0:
        radio=mayor()
    print(f"El área del círculo es: {area_circulo(radio):.2f}")
    
    altura = float(input("Introduce la altura del cilindro: "))
    if altura < 0:
        altura=mayor()
    print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura):.2f}")

if __name__ == "__main__":
    main()
