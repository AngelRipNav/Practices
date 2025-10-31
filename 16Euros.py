#Ejercicio 40: Dada una cantidad de euros (múltiplo de 5) realizar el desglose de billetes (500,200,100,50,20,10,5), siempre intentando dar el mínimo de billetes posible.

def main():
    euro = int(input("Introduce un numero de euros: "))

    adiv = 0
    b500 = 0
    b200 = 0
    b100 = 0
    b50 = 0
    b20 = 0
    b10 = 0
    b5 = 0

    if euro %5 == 0:

        while euro != 0:
            if euro >= 500:
                b500 = b500 + 1
                euro = euro -500
            elif euro<500 and euro >= 200:
                b200 = b200 + 1
                euro = euro -200
            elif euro < 200 and euro >= 100:
                b100 = b100 + 1
                euro = euro -100
            elif euro < 100 and euro >= 50:
                b50 = b50 + 1
                euro = euro -50
            elif euro < 50 and euro >= 20:
                b20 = b20 + 1
                euro = euro -20
            elif euro < 20 and euro >= 10:
                b10 = b10 + 1
                euro = euro -10
            elif euro < 10 and euro >= 5:
                b5 = b5 + 1
                euro = euro -5
        print(f"En total he dado {b500} billetes de 500 euros, {b200} billetes de 200 euros, {b100} billetes de 100 euros, {b50} billetes de 50 euros, {b20} billetes de 20 euros, {b10} billetes de 10 euros, {b5} billetes de 5 euros")
    else:
        print("No puedo darte monedas pon un numero multiplo de 5")
if __name__ == "__main__":
    main()
