
from utils import *

def calcular_precio(casa):
    #Calcular precio funcion
    anyo_actual = 2026
    #Calcular antiguedad
    antiguedad = anyo_actual - casa['año']
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

def muestraCasa(casa):
    #Menu para mostrar las casas
    print("Año de consturcción:",casa['año'])
    print("Metros:",casa['metros'])
    print("Habitaciones:",casa['habitaciones'])
    if casa['garaje']:
        print("Tiene Garaje")
    else:
        print("No tiene Garaje")
    print("Zona:",casa['zona'])
    print("Precio:",casa['precio'])

def add_inm(inmuebles): 
    #Menu para añadir inmuebles
    print("\n--- AÑADIR INMUEBLE ---")
    anyo = pedir_num_extra(1900, 2026, "Año de construcción: ")
    metros = pedir_num_extra(50, 1000, "Metros cuadrados: ")
    habitaciones = pedir_num_extra(1, 20, "Número de habitaciones: ")
    garaje = si_no("Tiene Garaje (Si o No): ")
    zona = input("Zona (A o B): ").upper()
    while zona not in ['A', 'B']:
        print("La zona debe ser A o B")
        zona = input("Zona (A o B): ").upper()
    
    nuevo_inmueble = {
        'año': anyo,
        'metros': metros,
        'habitaciones': habitaciones,
        'garaje': bool(garaje),
        'zona': zona
    }
    inmuebles.append(nuevo_inmueble)
    print("Inmueble añadido correctamente")

def bus_inm(anyo, metros, inmuebles):
    # Menu para buscar inmuebles con año y metros y me debe devolver la casa (no habran 2 del mismo año y los mismos metros)
    contador = 0
    enc = False
    inmueble_encontrado = None
    indice_encontrado = None
    
    while (not enc and contador < len(inmuebles)):
        if inmuebles[contador]['año'] == anyo and inmuebles[contador]['metros'] == metros:
            inmueble_encontrado = inmuebles[contador]
            indice_encontrado = contador
            enc = True
        contador += 1
    
    return inmueble_encontrado, indice_encontrado

def show_inm(inmuebles):
    #Menu para mostrar inmuebles
    print("\n--- TODOS LOS INMUEBLES ---")
    if len(inmuebles) == 0:
        print("No hay inmuebles disponibles")
        
    else:
        print(f"\nTotal de inmuebles: {len(inmuebles)}\n")
        print("=" * 40)
        contador = 1
        for casa in inmuebles:
            print(f"\nINMUEBLE #{contador}")
            casa_copia = casa.copy()
            casa_copia['precio'] = f'{calcular_precio(casa):.2f}€'
            muestraCasa(casa_copia)
            print("-" * 40)
            contador = contador + 1
        print("=" * 40)
    return

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
        print("\n" + "=" * 35)
        print("  MENÚ DE GESTIÓN DE INMUEBLES")
        print("=" * 35)
        print("1. Añadir un inmueble")
        print("2. Borrar un inmueble")
        print("3. Buscar un inmueble")
        print("4. Mostrar todos los inmuebles")
        print("5. Inmuebles x presupuesto")
        print("6. Salir")
        print("=" * 35)
        opcion = pedir_numero(1,6)
        if opcion == 1:
            add_inm(inmuebles)
        elif opcion == 2:
            print("\n--- BORRAR INMUEBLE ---")
            if len(inmuebles) == 0:
                print("No hay inmuebles disponibles")
            else:
                anyo = pedir_num_extra(1900, 2026, "Año de construcción: ")
                metros = pedir_num_extra(50, 1000, "Metros cuadrados: ")
                inmueble_encontrado, indice_encontrado = bus_inm(anyo, metros, inmuebles)         
                if inmueble_encontrado != None:
                    inmuebles.pop(indice_encontrado)
                    print("Inmueble borrado correctamente")
                else:
                    print("No se encontraron inmuebles con esas características")
        
        elif opcion == 3:
            print("\n--- BUSCAR INMUEBLE ---")
            if len(inmuebles) == 0:
                print("No hay inmuebles disponibles")
            else:
                anyo = pedir_num_extra(1900, 2026, "Año de construcción: ")
                metros = pedir_num_extra(50, 1000, "Metros cuadrados: ")
                inmueble_encontrado, indice_encontrado = bus_inm(anyo, metros, inmuebles)         
                if inmueble_encontrado == None:
                    print("No se encontraron inmuebles con esas características")
                else:
                    print("-" * 40)
                    print("Inmueble encontrado:\n")
                    casa_copia = inmueble_encontrado.copy()
                    casa_copia['precio'] = f'{calcular_precio(inmueble_encontrado):.2f}€'
                    muestraCasa(casa_copia)
                    print("-" * 40)

        elif opcion == 4:
            show_inm(inmuebles)
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
            salir = True



if __name__ == "__main__":
    main()

