'''El hotel tiene varias habitaciones, cada una con un número de identificación único, un tipo (individual, doble, suite) y un estado (disponible, reservada, no disponible).

La estructura de habitaciones del hotel será una lista de diccionarios, cada elemento de la lista será un diccionario que corresponde con una habitación del hotel. Los datos de cada habitación serán: número, tipo y estado.

El sistema debe permitir:

Mostrar todas las habitaciones disponibles.
Hacer una nueva reserva si la habitación está disponible.
Mostrar todas las habitaciones reservadas.
Salir
Función para mostrar habitaciones disponibles.
Función para mostrar habitaciones reservadas.
Escribe una función para verificar si dado un número de habitación está disponible.
Escribe una función para reservar, debe recibir dos argumentos:
La lista de habitaciones del hotel.
Tipo de habitación: El tipo de habitación que busca el cliente (solo puede ser "individual", "doble" o "suite").
La función debe:

1.- cambiar el estado de la habitación reservada si se ha podido reservar

2.- devolver el número de habitación reservada (-1 en caso de no haber habitación disponible)

Reglas de reserva:

Solo se puede reservar una habitación si está disponible.
Si no hay habitaciones disponibles del tipo solicitado, se debe indicar que no hay disponibilidad.'''

from utils import *

def buscar(hotel, numHabi):
    nh={}
    enc=False
    cont = 0
    while (cont < len(hotel) and not enc):
        habi = hotel[cont]
        if habi["numero"] == numHabi:
            nh=habi
            enc=True
        else:
            cont=cont+1
    return nh

def reservar_habitacion(hotel, habitacion):
    reservada=False
    if habitacion["estado"] == "Disponible":
        habitacion["estado"] = "Reservada"
        reservada = True
    else:
        reservada = False
    return reservada

def crear_habitacion(hotel):
    habitacion={}
    seguir = True
    tipos = ["Individual", "Doble", "Suite"]
    estados = ["Disponible", "Reservada", "No disponible"]
    while seguir:
        numero = int(input("Introduce el número de habitación: "))
        #Asegurarse de que el número de habitación no existe para evitar duplicas
        if buscar(hotel, numero):
            print("\n¡El número de habitación ya existe!\n")
        else:
            seguir = False

    tipo = pedir_Num_Premium(1, 3, "\nIntroduce el tipo de habitación: \n1-individual \n2-doble \n3-suite\n\nSelecciona el tipo (1-3): ")
    estado = pedir_Num_Premium(1, 3, "\nIntroduce el estado de la habitación: \n1-disponible \n2-reservada \n3-no disponible\n\nSelecciona el estado (1-3): ")
    precio = float(input("\nIntroduce el precio de la habitación: "))
    habitacion["numero"] = numero
    habitacion["tipo"] = tipos[tipo-1]
    habitacion["estado"] = estados[estado-1]
    habitacion["precio"] = precio
    return habitacion

def anadir_habitacion(hotel, habitacion):
    hotel.append(habitacion)
    anadida = True
    return anadida

def mostrar_habitaciones(hotel):
    print("\n" + "="*60)
    print(f"{'HABITACIONES':<16} {'TIPO':<15} {'ESTADO':<17} {'PRECIO':<15}")
    print("="*60)
    indice = 1
    for habitacion in hotel:
        print(f"{habitacion['numero']:<15} {habitacion['tipo']:<15} {habitacion['estado']:<15} {habitacion['precio']:>8.2f} €")
        indice = indice + 1

def mostrarMenu(menu):
    for op in menu:
        print(op)

def most_hab_hotel(hotel):
    print("\n" + "="*60)
    print(f"{'HABITACIONES':<16} {'TIPO':<15} {'ESTADO':<17} {'PRECIO':<15}")
    print("="*60)
    indice = 1
    for habitacion in hotel:
        if habitacion["estado"] == "Reservada":
            print(f"{habitacion['numero']:<15} {habitacion['tipo']:<15} {habitacion['estado']:<15} {habitacion['precio']:>8.2f} €")
            indice = indice + 1

def main():
    hotel = []
    menu = ["1. Añadir habitación",
            "2. Mostrar todas habitaciones",
            "3. Hacer una reserva",
            "4. Mostrar habitaciones reservadas",
            "5. Salir"]
    seguir = True
    while seguir:
        print("\n" + "="*60)
        print("SISTEMA DE RESERVA DE HABITACIONES")
        print("="*60)
        mostrarMenu(menu)
        op = pedir_num_extra(1, 5, "\nSelecciona una opción")
        #Alta de habitaciones
        if op ==1:
            print("\n" + "="*60)
            print("Añadir habitación")
            print("="*60)
            habit=crear_habitacion(hotel)
            exito=anadir_habitacion(hotel, habit)
            if exito:
                print("\nHabitación añadida correctamente")
            else:
                print("\nError al añadir la habitación")

        #Mostrar todas las habitaciones
        if op == 2:
            mostrar_habitaciones(hotel)

        #Hacer una reserva
        if op == 3:
            numero = int(input("\nIntroduce el número de habitación: "))
            habitacion = buscar(hotel, numero)
            if not habitacion:
                print("\nError al reservar la habitación")
            else:
                reservada = reservar_habitacion(hotel, habitacion)
                if reservada:
                    print("\nHabitación reservada correctamente")
                else:
                    print("\nError al reservar la habitación")

        #Mostrar habitaciones reservadas
        if op == 4:
            most_hab_hotel(hotel)
        #Salir
        if op == 5:
            seguir = False
    print()

if __name__ == "__main__":
    main()
