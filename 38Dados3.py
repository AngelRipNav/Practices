#Ejercicio 61: Escriba un programa que muestre tres números al azar del 1 al 6.

def main():
    import random
    
    moneda=1

    contador= input("Pulse Intro para iniciar el juego: ")

    while contador=="":    
        dado1=random.randrange(1,7)
        dado2=random.randrange(1,7)
        dado3=random.randrange(1,7)

        print(f"Tirada: {dado1} {dado2} {dado3}")

        if (dado1 == dado2) and (dado2==dado3):
            moneda=moneda+4
            print(f"Has ganado  5 monedas, ahora tienes un total de {moneda} monedas")
        elif (dado1 == dado2) or (dado2==dado3) or (dado1==dado3):
            moneda=moneda+1
            print(f"Has ganado 2 monedas, ahora tienes un total de {moneda} monedas")
        else:
            moneda=moneda-1
            print(f"No has ganado nada, ahora tienes un total de  {moneda} monedas")

        contador=input("Pulse Intro para volver a jugar, otra tecla e Intro para terminar: ")

    print("Programa terminado")

if __name__ == "__main__":
    main()
