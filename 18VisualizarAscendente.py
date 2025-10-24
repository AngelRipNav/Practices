#Actividad 18: Programar la lectura y visualizacion de 2 numeros y ordenarlos de manera ascendente

def main():
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    if num1 < num2:
        print(f"{num2}")
        print(f"{num1}")
    else:
        print(f"{num1}")
        print(f"{num2}")
if __name__ == "__main__":
    main()