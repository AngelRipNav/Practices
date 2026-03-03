'''Ejercicio Lista 5
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5'''

from util import *

def calcular_precio(casa):
    #Calcular precio funcion
    año_actual = 2026
    #Calcular antiguedad
    antiguedad = año_actual - casa['año']
    #Calcular precio base
    precio_base = (casa['metros'] * 1000 + 
                  casa['habitaciones'] * 5000 + 
                  casa['garaje'] * 15000)
    
    if casa['zona'] == 'A':
        precio = precio_base * (1 - antiguedad / 100)
    else:  # Zona B
        precio = precio_base * (1 - antiguedad / 100) * 1.5
    
    return precio

def buscar_inmuebles(inmuebles, presupuesto):
    #Buscar inmuebles
    inmuebles_disponibles = []
    for casa in inmuebles:
        precio = calcular_precio(casa)
        
        if precio <= presupuesto:
            casa_con_precio = casa
            casa_con_precio['precio'] = f'{precio:.2f}€'
            inmuebles_disponibles.append(casa_con_precio)
    
    return inmuebles_disponibles

def añadir_inmueble(inmuebles):
    """Añade un nuevo inmueble a la lista"""
    print("\n--- AÑADIR INMUEBLE ---")
    año = pedir_num_extra(1900, 2026, "Año de construcción: ")
    metros = pedir_num_extra(1, 1000, "Metros cuadrados: ")
    habitaciones = pedir_num_extra(1, 20, "Número de habitaciones: ")
    garaje = pedir_num_extra(0, 1, "¿Tiene garaje? (1=Sí, 0=No): ")
    zona = input("Zona (A o B): ").upper()
    while zona not in ['A', 'B']:
        print("Error: La zona debe ser A o B")
        zona = input("Zona (A o B): ").upper()
    
    nuevo_inmueble = {
        'año': año,
        'metros': metros,
        'habitaciones': habitaciones,
        'garaje': bool(garaje),
        'zona': zona
    }
    inmuebles.append(nuevo_inmueble)
    print("✓ Inmueble añadido correctamente")

def borrar_inmueble(inmuebles):
    """Borra un inmueble de la lista"""
    print("\n--- BORRAR INMUEBLE ---")
    if len(inmuebles) == 0:
        print("No hay inmuebles para borrar")
        return
    
    print(f"Hay {len(inmuebles)} inmuebles:")
    for i, casa in enumerate(inmuebles):
        print(f"{i+1}. Año: {casa['año']}, Metros: {casa['metros']}, Habitaciones: {casa['habitaciones']}, Zona: {casa['zona']}")
    
    indice = pedir_numero(1, len(inmuebles), "Número del inmueble a borrar: ")
    inmuebles.pop(indice - 1)
    print("✓ Inmueble borrado correctamente")

def buscar_inmueble(inmuebles):
    """Busca y muestra un inmueble específico"""
    print("\n--- BUSCAR INMUEBLE ---")
    if len(inmuebles) == 0:
        print("No hay inmuebles disponibles")
        return
    
    print(f"Hay {len(inmuebles)} inmuebles")
    indice = pedir_numero(1, len(inmuebles), "Número del inmueble a buscar: ")
    casa = inmuebles[indice - 1]
    casa_copia = casa.copy()
    casa_copia['precio'] = f'{calcular_precio(casa):.2f}€'
    print("\n" + "-" * 40)
    muestraCasa(casa_copia)
    print("-" * 40)

def mostrar_inmuebles(inmuebles):
    print("\n--- TODOS LOS INMUEBLES ---")
    if len(inmuebles) == 0:
        print("No hay inmuebles disponibles")
        return
    
    print(f"\nTotal de inmuebles: {len(inmuebles)}\n")
    print("=" * 40)
    for i, casa in enumerate(inmuebles):
        print(f"\nINMUEBLE #{i+1}")
        casa_copia = casa.copy()
        casa_copia['precio'] = f'{calcular_precio(casa):.2f}€'
        muestraCasa(casa_copia)
        print("-" * 40)
    print("=" * 40)

def muestraCasa(casa):
    print("Año de consturcción:",casa['año'])
    print("Metros:",casa['metros'])
    print("Habitaciones:",casa['habitaciones'])
    if casa['garaje']:
        print("Tiene Garaje")
    else:
        print("No tiene Garaje")
    print("Zona:",casa['zona'])
    print("Precio:",casa['precio'])

def main():
    #Inmuebles
    inmuebles = [
        {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
        {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
        {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
        {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
        {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

    salir=False
    while not salir:
        print("\n" + "=" * 40)
        print("  MENÚ DE GESTIÓN DE INMUEBLES")
        print("=" * 40)
        print("1. Añadir un inmueble")
        print("2. Borrar un inmueble")
        print("3. Buscar un inmueble")
        print("4. Mostrar todos los inmuebles")
        print("5. Inmuebles x presupuesto")
        print("6. Salir")
        print("=" * 40)
        opcion = pedir_numero(1,6)
        if opcion == 1:
            añadir_inmueble(inmuebles)
        elif opcion == 2:
            borrar_inmueble(inmuebles)
        elif opcion == 3:
            buscar_inmueble(inmuebles)
        elif opcion == 4:
            mostrar_inmuebles(inmuebles)
        elif opcion == 5:
            print("\n--- BÚSQUEDA POR PRESUPUESTO ---")
            presupuesto = pedir_precio(0, 1000000)
            inmuebles_encontrados = buscar_inmuebles(inmuebles, presupuesto)
            
            print(f"\nInmuebles encontrados con presupuesto de {presupuesto}€:\n")
            print("=" * 40)
            if len(inmuebles_encontrados) == 0:
                print("No se encontraron inmuebles con ese presupuesto")
            else:
                for casa in inmuebles_encontrados:
                    muestraCasa(casa)
                    print("-" * 40)
            print("=" * 40)
        elif opcion == 6:
            print("\n¡Hasta pronto!")
            salir = True

if __name__ == "__main__":
    main()
