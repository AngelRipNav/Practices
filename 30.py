#Ejercicio 52:Escribir un programa que me ayude a aprender las tablas de multiplicar.

#Para ello se irá pidiendo la tabla de multiplicar de un número (pedido por teclado con anterioridad) y comprobando que los valores introducidos son correctos. Si es así el programa escribirá "CORRECTO" y en caso contrario deberá escribir "LO SIENTO, SE HA EQUIVOCADO. LA RESPUESTA CORRECTA ES número".

#La última línea mostrará el número de aciertos.

def main():
    num=int(input("Introduce un numero entero positivo: "))
    mult = 1
    for i in range (1,11):
        print(f"{num}*{mult} =", num*mult)
        mult = mult +1    

if __name__ == "__main__":
    main()
