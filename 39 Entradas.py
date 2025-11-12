
#Un parque temático ofrece distintos precios de entrada según la edad de los visitantes y el día de la semana. Los precios base son los siguientes: 

#Entrada general: 60€ por persona.

#Tarifas especiales:


#Niños menores de 5 años entran gratis.
#Los niños entre 5 y 12 años reciben un 50% de descuento en cualquier día.
#Los jóvenes entre 13 y 17 años obtienen un 20% de descuento de lunes a viernes y un 30% de descuento los fines de semana.
#Los adultos mayores de 65 años tienen un 40% de descuento en cualquier día.
#El programa debe calcular el coste total de las entradas para un grupo de visitantes.


#Se debe leer el nombre, la edad de cada visitante y el día de la visita, como texto (lunes, martes, etc.).


#El programa debe pedir al usuario que introduzca el número de visitantes o preguntar después de cada entrada si hay más personas en el grupo (elige y comenta la opción).

#Extra: Una vez calculado el precio para el grupo, el programa debe mostrar el coste total y preguntar si se desea calcular el precio para otro grupo.


def main():
    grup=True
    while grup:
        entradast=0
        precio=60
        entrada=0
        pos=True
        sem=True
        while pos:
            num1=int(input("Cuantas entradas piensas comprar: "))
            if num1 >= 0:
                pos=False
            else:
                print("¡Asegurese que sea un numero positivo!\n")


        while sem:
            print("Que dia de la semana quiere reservar: L, Ma, Mi, J, V, S, D:", end=" ")
            dia=input("")
            
            if dia == "L" or dia== "Ma" or dia== "Mi" or dia== "J" or dia== "V" or dia== "S" or dia=="D":
                sem=False

            else:
                print("¡Introduzca un numero de la semana correcto!\n")


        for i in range (1, num1+1):

            nom=input("\nCual es su nombre: ")

            edad=int(input(f"\nCual es la edad del {i}º visitante: "))

            if edad < 5:
                print(f"La entrada es gratuita")
                entrada=entrada+1
                preciotemp=0

            elif edad >=5 and edad <=12:
                entrada=entrada+1
                preciotemp=precio-(precio * 0.5)
                print("La entrada tiene un 50% de descuento")

            elif edad >=13 and edad<=17:
                if dia == "L" or dia == "Ma" or dia == "Mi" or dia== "J" or dia== "V":
                    print("La entrada tiene un 20% de descuento")
                    entrada=entrada+1
                    preciotemp=precio-(precio * 0.2)

                else:
                    print("La entrada tiene un 30% de descuento")
                    entrada=entrada+1
                    preciotemp=precio-(precio * 0.3)

            elif edad >65:
                print("La entrada tiene un 40% de descuento")
                entrada=entrada+1
                preciotemp=precio-(precio * 0.4)

            else:
                print("Se pagara el precio completo")
                preciotemp=precio

            entradast= entradast+preciotemp

            print(f"{nom} pagara {preciotemp} y vendra el {dia}")

        print(f"El grupo en total pagara {entradast} y vendra el {dia}")

        entra=input("Quiere comprar las entradas de otro grupo: Si | No: ")
        if entra== "No" or entra=="N" or entra=="no" or entra=="n":
            grup= False
    
if __name__ == "__main__":
    main()
