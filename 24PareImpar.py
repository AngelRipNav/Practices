#Ejercicio 47: Par e Impar

def main():
    impar=0
    par=0
    for i in range(1,16):    
        num = int(input("Introduce un numero entero positivo: "))
        if num % 2 == 0:
            par = par +1
            print ("Este numero es par")
        else:
            impar = impar +1
            print ("Este numero es impar")
    print (f"Ha habido un total de {par} pares y {impar} impares")


if __name__ == "__main__":
    main()
