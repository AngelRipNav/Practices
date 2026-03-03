#Funcion que comprueba que las respuestas sean si o no
def si_no(m):
    bucle = True
    while bucle:
        respuesta = input(m).strip().lower()
        if respuesta == "si" or respuesta == "no":
            bucle=False
        else:
            print("\nError: La respuesta tiene que ser si o no\n")
    return respuesta


#Pedir un numero
def pedir_numero(x, y):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número entre {x} y {y}: "))
        if numero >= x and numero <= y:
            seguir = False
        else:
            print(f"Error: El número debe estar entre {x} y {y}.\n")
    return numero


#Pedir un numero mayor a
def mayor(x):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un número (superior a {x}): "))
        if numero > x:
            seguir = False
        else:
            print(f"Error: El número debe superior a {x}.\n")
    return numero


#Pedir precio directamente sin tener que meter el z
def pedir_precio(x, y):
    seguir = True
    while seguir:
        numero = int(input(f"Introduce un precio entre {x} y {y}: "))
        if numero > x and numero <= y:
            seguir = False
        else:
            print(f"Error: El precio debe estar entre {x} y {y}.\n")
    return numero



#Pedir numero e introducir de que tipo de numero quiero pedir
def pedir_num_extra(x, y, z):
    seguir = True
    while seguir:
        numero = int(input(f"{z} entre {x} y {y}: "))
        if numero >= x and numero <= y:
            seguir = False
        else:
            print(f"El número debe estar entre {x} y {y}.\n")
    return numero


#Cuando quiera calcular un precio
def calcular_subtotal(precio, cantidad):
    #Calcula el subtotal del producto
    return precio * cantidad



#Utilizar para catalogos de productos
def mostrar_catalogo(x):
    #Muestra el catálogo de productos disponibles
    print("\n" + "="*60)
    print("CATÁLOGO DE PRODUCTOS")
    print("="*60)
    
    indice = 1
    for producto in x:
        print(f"{indice}. {x['nombre']:<40} {x['precio']:>8.2f} €")
        indice = indice + 1
    
    print("="*60 + "\n")


def mostrar_catalogo_premium(x):
    #Muestra el catálogo de productos disponibles
    indice = 1
    for producto in x:
        print(f"{indice}. {x['numero']:<40}, {x['tipo']:<20}, {x['estado']:<20}, {x['precio']:>8.2f} €")
        indice = indice + 1

def pedir_Num_Premium(x, y, z):
    seguir = True
    while seguir:
        numero = int(input(f"\n{z}"))
        if numero >= x and numero <= y:
            seguir = False
        else:
            print(f"El número debe estar entre {x} y {y}.\n")
    return numero

'''
<40 - Alineación a la izquierda con 40 espacios
nombre = "Ratón"
print(f"{nombre:<40}")  # "Ratón                                   "

< = alinear a la izquierda
40 = reservar 40 caracteres de espacio
Si el texto es más corto, rellena con espacios a la derecha

>8.2f - Alineación a la derecha para números decimales
precio = 25.5
print(f"{precio:>8.2f}")  # "   25.50"

> = alinear a la derecha
8 = reservar 8 caracteres de espacio
.2 = mostrar 2 decimales
f = formato de número decimal (float)

Ejemplo visual completo:
producto1 = "Ratón"
precio1 = 25.5

producto2 = "Monitor LED 24\" Full HD"
precio2 = 129.0

print(f"{producto1:<40} {precio1:>8.2f} €")
print(f"{producto2:<40} {precio2:>8.2f} €")
```

**Salida:**
```
Ratón                                       25.50 €
Monitor LED 24" Full HD                    129.00 €
¿Ves cómo queda todo alineado? Eso es lo que hacen esos símbolos: crear columnas ordenadas.
Si quieres simplificarlo, puedes escribir simplemente:
pythonprint(f"{producto['nombre']} {producto['precio']:.2f} €")
'''



def main():
    print()


if __name__ == "__main__":
    main()
