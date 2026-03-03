'''Ejercicio 1: Sistema de facturación de una tienda
Estás desarrollando un sistema sencillo para una tienda que vende productos. El sistema debe calcular el total a pagar por un cliente en función de la cantidad de productos que compra. Cada producto tiene un precio fijo, y el sistema debe aplicar un descuento si el total supera una cierta cantidad.
Instrucciones:

La función debe recibir el precio de un producto y la cantidad comprada.
Si el total supera los 100 (el precio total sin descuento), se debe aplicar un descuento del 10%.
La función debe devolver el precio final a pagar.
El programa principal debe pedir productos hasta que cliente decida terminar.
'''

from utils import *

def calcular_subtotal(precio, cantidad):
    #Calcula el subtotal del producto
    return precio * cantidad

def main():
    # Catálogo de productos
    PRODUCTOS = [
        {"nombre": "Ratón Inalámbrico Ergonómico", "precio": 25.50},
        {"nombre": "Teclado Mecánico RGB", "precio": 64.99},
        {"nombre": "Monitor LED 24\" Full HD", "precio": 129.00},
        {"nombre": "Auriculares con Cancelación de Ruido", "precio": 89.95},
        {"nombre": "Alfombrilla de Escritorio XL", "precio": 15.20},
        {"nombre": "Memoria USB 128GB (3.1)", "precio": 18.75},
        {"nombre": "Soporte para Portátil Ajustable", "precio": 32.40},
        {"nombre": "Cámara Web 1080p", "precio": 45.00}
    ]

    total_compra = 0.0
    
    print("¡Bienvenido al sistema de facturación!")
    seguir = True
    while seguir:
        mostrar_catalogo(PRODUCTOS)
        # Seleccionar producto
        codigo = pedir_num_extra(1, len(PRODUCTOS), "Ingrese el código del producto: ")
        producto_seleccionado = PRODUCTOS[codigo - 1]  # Ajustar índice (la lista va del 0 al 7, pero la persona va a pner del 1 a 8)
        
        print(f"\nProducto seleccionado: {producto_seleccionado['nombre']}")
        print(f"Precio unitario: {producto_seleccionado['precio']:.2f} €")
        
        # Pide la cantidad
        cantidad = pedir_num_extra(1, 100, "Cantidad: ")
        
        # Calcula el subtotal del producto
        subtotal_producto = calcular_subtotal(producto_seleccionado['precio'], cantidad)
        
        # Mostrar el resultado NO FINAL SI NO DEL PRODUCTO
        print(f"\n{'─'*50}")
        print(f"Subtotal producto: {subtotal_producto:.2f} €")
        print(f"{'─'*50}\n")
        
        total_compra += subtotal_producto
        
        # Preguntar si si o no
        respuesta = si_no("¿Desea agregar otro producto? (Si o No): ")
        
        if respuesta == "no":
            # Aplicar descuento al total final si supera los 100 pavos
            descuento_aplicado = False
            total_final = total_compra
            
            if total_compra > 100:
                total_final = total_compra * 0.9
                descuento_aplicado = True
            
            print("\n" + "="*60)
            print(f"Subtotal de la compra: {total_compra:.2f} €")
            if descuento_aplicado:
                print(f"Descuento aplicado (10%): -{total_compra * 0.1:.2f} €")
                print(f"TOTAL FINAL: {total_final:.2f} €")
            else:
                print(f"TOTAL FINAL: {total_final:.2f} €")
            print("="*60)
            print("¡Gracias por su compra! Hasta luego.")
            seguir = False

if __name__ == "__main__":
    main()
