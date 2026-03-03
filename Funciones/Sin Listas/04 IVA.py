#Ejercicio 04: Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def mayor():
    x=False
    print('\nNO SE PUEDE RESOLVER VUELVE A INTRODUCIRLO\n')
    while not x:
        n=int(input("Introduce un número entero positivo: "))
        if n < 0: 
            print('\nNO SE PUEDE RESOLVER VUELVE A INTRODUCIRLO\n')
        else:
            x=True
    return n

def iva(cantidad, porcentaje=21):
    return cantidad + (cantidad * porcentaje / 100)

def main():
    cant = float(input("Introduce la cantidad: "))
    if cant < 0:
        cant=mayor()
    print("El total de la factura es: ", iva(cant))        

if __name__ == "__main__":
    main()
