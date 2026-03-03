'''
Programa que escribe la tabla de multiplicar de un número introducido por teclado.

El programa debe tener:

Una función que pida un número > 0 y <=10, y lo devuelva cuando sea correcto
Una función que recibe como argumento el número entero anterior y muestra la tabla de multiplicar de dicho número.
'''

def pedir_numero(x, y):

    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número ({x}-{y}): "))
        if numero > x and numero <= y:
            seguir = False
        else:
            print(f"Error: El número debe estar entre {x} y {y}.\n")
    return numero

def mostrar_tabla(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("-" * 20)

def main():
    numero = pedir_numero(0,10)
    mostrar_tabla(numero)


if __name__ == "__main__":
    main()
