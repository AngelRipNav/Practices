#Ejercicio 07: Algoritmo que lee 100 numeros no nulos y dice cuantos positivos y cuantos negativos

def main():
    negativos = 0
    positivos = 0
    for i in range(100):
        num=int(input("Introduce un numero no nulo: "))
        if num < 0:
            negativos = negativos + 1
        else:
            positivos = positivos + 1
    print(f"Hay {positivos} positivos y {negativos} negativos")

if __name__ == "__main__":
    main()