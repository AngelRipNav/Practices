#DIVISION,SUMA,RESTA,MULTIPLICAICON Y RESTO, TENIENDO EN CUENTA EL 0

def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    suma = num1 + num2
    resta = num1 - num2
    mult = num1 * num2
    print(f"La suma de {num1} + {num2} es: {suma}")
    print(f"La resta de {num1} - {num2} es: {resta}")
    print(f"La multiplicacion de {num1} * {num2} es: {mult}")
    if num2 != 0:
        print(f"La division de {num1} / {num2} es: {num1 / num2}")
        print(f"El resto de {num1} % {num2} es: {num1 % num2}")
    else:
        print("No se puede dividir entre 0 ni calcular el resto")

if __name__ == "__main__":
    main()

