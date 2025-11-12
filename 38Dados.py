#Ejercicio 61: Escriba un programa que muestre tres números al azar del 1 al 6.

def main():
    import random

    contador= input("Pulse Intro para iniciar el juego: ")

    while contador=="":
        
        dado1=random.randrange(1,7)
        dado2=random.randrange(1,7)
        dado3=random.randrange(1,7)

        print(f"Tirada: {dado1} {dado2} {dado3}")
        
        contador=input("Pulse Intro para volver a jugar, otra tecla e Intro para terminar: ")

    print("Programa terminado")
if __name__ == "__main__":
    main()
