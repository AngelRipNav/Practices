#Ejercicio 06: Algoritmo que lee 100 numeros no nulos y dice si ha visto algún número negativo o no.

def main():
    haynegativo=False
    for i in range(100):
        num=int(input("Introduce un numero no nulo: "))
        if num < 0:
            haynegativo=True
    if haynegativo:
        print("Se ha visto un numero negativo")
    else:
        print("No se ha visto ningun numero negativo")



if __name__ == "__main__":
    main()