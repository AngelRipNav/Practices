#Ejercicio 60: Escriba un programa que pida la cantidad de números positivos que se tienen que escribir y a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada.

def main():
    cnum = 0
    pos = 0
    
    numx=int(input("Escriba la cantidad de numeros positivos a escribir: "))
    while numx <= 0:
        numx=int(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))

    num1=int(input("Escriba un numero: "))
    cnum=cnum+1
    if num1 >=0:
        pos = pos + 1

    while numx != pos:
        num1=int(input("Escriba otro numero: "))
        cnum= cnum +1

        if num1 >=0:
            pos = pos + 1

    print(f"{cnum} numeros totales y {pos} positivos")


if __name__ == "__main__":
    main()
