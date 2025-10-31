#Actividad 22: Programa que lee tres números cualesquiera y nos indica todas sus relaciones de igualdad

def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num3 = float(input("Introduce el tercer numero: "))
    if num1 == num2:
        if num2 == num3:
            print("Los tres numeros son iguales")
        else:
            print("Los dos primeros numeros son iguales y el tercero no")
    else: 
        if num2 == num3:
            print("Los dos ultimos numeros son iguales y el primero no")
        elif num1 == num3:
            print("El primer y tercer numero son iguales y el tercero no")
        else:
            print("Ningun numero es igual")


if __name__ == "__main__":
    main()