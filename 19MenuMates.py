#Ejercicio 43: Algoritmo de un programa que muestra un menú con las siguientes opciones:
#Suma.
#Resta.
#Multiplicación.
#División.
#Salir.
#Y permite hacer las operaciones con dos numeros hasta que pulsemos la opción de salir.


def main():

    salir = False
    while not salir:
        print("Elija una de las siguientes opaciones \n Sumar \n Restar \n Multiplicar \n Dividir \n Salir" )
        opc=input("")
        if opc == "Sumar":
            num1=int(input("Selecciona tu primer numero: "))
            num2=int(input("Selecciona tu segundo numero: "))
            suma=num1+num2
            print(f"La suma de {num1} + {num2} resulta en {suma}")
        elif opc == "Restar":
            num1=int(input("Selecciona tu primer numero: "))
            num2=int(input("Selecciona tu segundo numero: "))
            resta=num1-num2
            print(f"La resta de {num1} - {num2} resulta en {resta}")
        elif opc == "Multiplicar":
            num1=int(input("Selecciona tu primer numero: "))
            num2=int(input("Selecciona tu segundo numero: "))
            mult=num1*num2
            print(f"La multiplicacion de {num1} * {num2} resulta en {mult}")
        elif opc == "Dividir":
            num1=int(input("Selecciona tu primer numero: "))
            num2=int(input("Selecciona tu segundo numero: "))
            if num2 != 0:
                divis=num1/num2
                print(f"La division de {num1} / {num2} resulta en {divis}")
            else:
                print("No puedo dividir por 0")
        else:
            salir=True



if __name__ == "__main__":
    main()
