#Ejercicio 05: Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
import math

def rango(x, y):
    seguir = True
    while seguir:
        valor = float(input("Introduce un número: "))
        if valor >= x and valor <= y:
            seguir = False
        else:
            print(f"Error: El valor debe estar entre {x} y {y}.\n")
    return valor

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

def main():
    radio = rango(0,200)
    print(f"El área del círculo es: {area_circulo(radio):.2f}")
    
    altura = rango(0,200)
    print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura):.2f}")

if __name__ == "__main__":
    main()
