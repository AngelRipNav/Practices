#Ejercicio 37: Algoritmo que calcule el valor de elevar un número real, A, a un número exponente entero, B.

def main():
    A = float(input("Introduce un número real (A): "))
    B = int(input("Introduce un número entero (B): "))
    resultado = 1.0

    if B >= 0:
        for _ in range(B):
            resultado = resultado * A
    else:
        for _ in range(-B):
            resultado = resultado / A

    print(f"{A} elevado a la {B} es {resultado}")


if __name__ == "__main__":
    main()
