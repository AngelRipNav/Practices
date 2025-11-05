#Ejercicio 45.1: Contar del numero pedido hasta el numero que introduzca el usuario
def main():
    num=int(input("Introduce un numero entero positivo: "))
    contador=0
    while contador <= num:
        print(contador, end=" ")
        contador= contador+1
    print()  # Salto de linea al final

if __name__ == "__main__":
    main()
