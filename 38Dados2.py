#Ejercicio 61: Escriba un programa que muestre tres números al azar del 1 al 6.

def main():
    import random

    contador= input("Pulse Intro para iniciar el juego: ")

    while contador=="":
        
        dado1=random.randrange(1,7)
        dado2=random.randrange(1,7)
        dado3=random.randrange(1,7)

        print(f"Tirada: {dado1} {dado2} {dado3}")

        if (dado1 == dado2) and (dado2==dado3):
            print("Hay tres numeros iguales")
        elif (dado1 == dado2) or (dado2==dado3) or (dado1==dado3):
            print("Hay dos numeros iguales")
        else:
            print("No hay numeros iguales")
        contador=input("Pulse Intro para volver a jugar, otra tecla e Intro para terminar: ")

    print("Programa terminado")
if __name__ == "__main__":
    main()
