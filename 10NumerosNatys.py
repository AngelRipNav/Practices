#Ejercicio 09: Algoritmo que calcula y escribe la suma y el producto de los 10 primeros números naturales.

def main():
    suma = 0
    prod = 1
    num = 1
    for num in range(1,11):
        suma = suma + num
        prod = prod * num
        num = num + 1
    print(f"La suma es {suma} y el producto es {prod}")

if __name__ == "__main__":
    main()