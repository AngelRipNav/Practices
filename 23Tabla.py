#Ejercicio 46: Programa que escribe la tabla de multiplicar de un número introducido por teclado.

def main():
    num=int(input("Introduce un numero entero positivo: "))
    mult = 1
    for i in range (1,11):
        print(f"{num}*{mult} =", num*mult)
        mult = mult +1    

if __name__ == "__main__":
    main()
