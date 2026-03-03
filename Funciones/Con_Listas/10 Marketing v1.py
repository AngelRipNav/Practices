'''
Ejercicio 5: Generador de mensajes personalizados para una campaña de marketing
Imagina que trabajas en una agencia de marketing y necesitas crear un sistema que genere mensajes personalizados para una campaña. El sistema debe tomar en cuenta el nombre del cliente, el producto que está promocionando y el descuento aplicable. El mensaje debe incluir un saludo con el nombre del cliente, la información sobre el producto y el porcentaje de descuento.

Instrucciones:

La función debe recibir tres argumentos:
nombre_cliente: El nombre del cliente.
producto: El nombre del producto que está en promoción.
descuento: El porcentaje de descuento que se aplica al producto.
La función debe devolver dos valores:
Un mensaje personalizado para el cliente, que incluya su nombre, el producto y el descuento.
Un mensaje indicando "¡No dejes pasar esta oferta!", pero si el descuento es superior al 20% "¡Este es un GRAN descuento para ti!"
Programa principal: terminará cuando el usuario decida acabar de comprobar descuentos.
'''

from utils import *

def generar_mensaje(nombre, produ, descue):
    msg_pers = f"¡Hola {nombre}, el {produ}, contiene un descuento del {descue}% !"
    if descue > 20:
        msg_ofer="¡Este es un GRAN descuento para ti!"
    else: 
        msg_ofer="¡No dejes pasar esta oferta!"
    return msg_pers, msg_ofer


def main():
    print("=" * 50)
    print("SISTEMA DE MARKETING - CAMPAÑA DE DESCUENTOS")
    print("=" * 50)
    seguir=True
    while seguir:
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        producto = input("Ingrese el nombre del producto: ")
        descuento = float(input("Ingrese el porcentaje de descuento: "))

        mensaje_personalizado, mensaje_oferta = generar_mensaje(nombre_cliente, producto, descuento)

        print("\n" + "=" * 50)
        print(mensaje_personalizado)
        print(mensaje_oferta)
        print("=" * 50)
        
        if si_no("Quieres introducir otro cliente (si/no): ") == "no":
            seguir=False

if __name__ == "__main__":
    main()
