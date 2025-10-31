##Ejercicio 33: Nos pide dos numeros y su producto, y despues comprueba si es correcto

def main():
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    producto = int(input("Pon el producto de ambos numeros: "))
    if producto == numero1 * numero2:
        print("Bien")
    else:
        print("Mal")
if __name__ == "__main__":
    main()