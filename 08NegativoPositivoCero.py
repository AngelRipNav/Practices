#Ejercicio 08: Algoritmo que lee una serie de numeros y dice cuantos positivos y cuantos negativos y termina cuando digo 0

def main():
    hayNeg = 0
    negativos = 0
    positivos = 0
    num=int(input("Introduce un numero: "))
    
    while num != 0:
        if num < 0:
            negativos = negativos + 1
            hayNeg = 1
        else:
            positivos = positivos + 1
        num=int(input("Introduce un numero: "))

    if hayNeg == 0:
        print(f"No han habido numeros negativos")
    else:
        print(f"Si hay numeros negativos")

    print(f"Han habido {negativos} negativos y {positivos} positivos")

if __name__ == "__main__":
    main()
