#Ejercicio 00:Pediremos numeros, y diremos cual es el doble del numero introducido.Pararemos cuando el numero introducido sea cero.

def main():
    num=int(input("Introduce un numero positivo (o 0): "))
    while num != 0:
        num1 = num * 2
        print(f"{num1} es el doble de {num}")
        num=int(input("Introduce un numero positivo (o 0): "))

if __name__ == "__main__":
    main()
