#Ejercicio 25: Descuento según el precio del producto.

def main():
    precio = float(input("Introduce el precio del producto: "))
    if precio < 6:
        descuento = 0
    elif precio < 60:
        descuento = 0.05
    else:
        descuento = 0.10
    precio_final = precio - (precio * descuento)
    print(f"El precio final es: {precio_final:.2f} euros")
if __name__ == "__main__":
    main()