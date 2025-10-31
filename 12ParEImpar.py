#Ejercicio 12: Algoritmo que suma independientemente los pares y los impares de los números comprendidos entre 100 y 200.

def main():
    nump = 100
    numn = 101
    numt = 100
    i = 100
    for i in range(100,201):
        if i % 2 == 0:
            nump = i + nump
        else:
            numn = numn + i
        numt = numt + i
    print (f"La suma de los numeros pares da {nump} y los numeros impares {numn} y en total da {numt}")

if __name__ == "__main__":
    main()
