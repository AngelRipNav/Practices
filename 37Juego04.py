#Ejercicio 37: Juego de cartas aleatorios, saca 3 cartas, gana puntuacion total mas alta, siempre que no pase de quince, si pasa, gana la otra persona automaticamente.

def main():
    import random
    hector = random.randrange(1, 10)
    hector2 = random.randrange(1, 10)
    hector3 = random.randrange(1, 10)
    gloria = random.randrange(1, 10)
    gloria2 = random.randrange(1, 10)
    gloria3 = random.randrange(1, 10)
    print("JUEGO DE CARTAS")
    print(f"Hector ha sacado un {hector}, un {hector2} y un {hector3}, total: {hector + hector2 + hector3}")
    print(f"Gloria ha sacado un {gloria}, un {gloria2} y un {gloria3}, total: {gloria + gloria2 + gloria3}")
    if (hector + hector2 + hector3) > 15 and (gloria + gloria2 + gloria3) > 15:
        print("No gana nadie")
    elif (hector + hector2 + hector3) > 15:
        print("Gana Gloria por que Hector se ha pasado de 15")
    elif (gloria + gloria2 + gloria3) > 15:
        print("Gana Hector por que Gloria se ha pasado de 15")
    elif (hector + hector2 + hector3) > (gloria + gloria2 + gloria3):
        print("Gana Hector")
    elif (gloria + gloria2 + gloria3) > (hector + hector2 + hector3):
        print("Gana Gloria")
    else:
        print("Empate")

if __name__ == "__main__":
    main()