#Ejercicio 47: Par e Impar pero me pide los dos numeros

def main():
    impar=0
    par=0
    num1 = int(input("Introduce un numero entero positivo: "))
    num2 = int(input("Introduce otro numero entero positivo: "))
    
    if num1 < num2:
        inicio = num1
        final = num2
    else:
        inicio = num2
        final = num1
        
    for i in range(inicio, final + 1):
        if i % 2 == 0:
            par = par +1
            print(f"El {i} es un numero es par")
        else:
            impar = impar +1
            print(f"El {i} es un numero es impar")
    print (f"Ha habido un total de {par} pares y {impar} impares")


if __name__ == "__main__":
    main()
