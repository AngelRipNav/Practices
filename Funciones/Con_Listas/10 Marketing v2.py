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

    PRODUCTOS = [
        {"nombre": "Ratón Inalámbrico Ergonómico", "producto": "Raton Wireless ergonómico con hasta 25600 de DPI", "descuento": 12},
        {"nombre": "Teclado Mecánico RGB", "producto": "Teclado mecanico 100% RGB con 7 patrones de colores distinto", "descuento": 15},
        {"nombre": "Monitor LED 24\" Full HD", "producto": "Monitor de alta calidad FULL HD, Led de 24\" ", "descuento": 20},
        {"nombre": "Auriculares con Cancelación de Ruido", "producto": "Auriculares con cancelacion de ruido y sonido envolvente", "descuento": 25},
        {"nombre": "Alfombrilla de Escritorio XL", "producto": "Alfombrilla XL de fibras de alta calidad", "descuento": 10},
        {"nombre": "Memoria USB 128GB (3.1)", "producto": "Memoria USB de 128GB de capacidad version 3.1 de alto calibre", "descuento": 10},
        {"nombre": "Soporte para Portátil Ajustable", "producto": "Soporte ajustable para portatil con con giro 360", "descuento": 15},
        {"nombre": "Cámara Web 1080p", "producto": "Camara de alta resolucion y alta gama", "descuento": 25}
    ]
    seguir = True
    while seguir:
        print("\n" + "="*60)
        print("CONSULTADOR DE DESCUENTOS")
        print("="*60)
        
        # Solicitar nombre del cliente
        nombre_cliente = input("\nIntroduce el nombre del cliente: ").strip()
        
        # Mostrar productos disponibles
        print("\n--- PRODUCTOS DISPONIBLES CON DESCUENTOS ---")

        i=1
        for prod in PRODUCTOS:
            print(f"{i}. {prod['nombre']}")
            i=i+1

        # Solicitar selección de producto
        seguir_prod = True
        while seguir_prod:
            opcion = int(input(f"\nSelecciona un producto (1-{len(PRODUCTOS)}): "))
            if 1 <= opcion and opcion <= len(PRODUCTOS):
                producto_seleccionado = PRODUCTOS[opcion - 1]["producto"]
                seguir_prod = False
            else:
                print(f"Introduce un número entre 1 y {len(PRODUCTOS)}")
        
        # Generar y mostrar los mensajes
        mensaje_personalizado, mensaje_oferta = generar_mensaje(nombre_cliente, producto_seleccionado, PRODUCTOS[opcion - 1]["descuento"])
        
        print("\n" + "-"*60)
        print("MENSAJE GENERADO:")
        print("-"*60)
        print(mensaje_personalizado)
        print(mensaje_oferta)
        print("-"*60)
        
        # Preguntar si desea continuar
        if si_no("Quieres introducir otro cliente (si/no): ") == "no":
            print("\n¡Gracias por usar el comprobador de descuentos!")
            seguir=False

if __name__ == "__main__":
    main()
