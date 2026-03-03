'''
La compañía de eléctrica X, desea calcular la tarifa a cobrar a sus clientes.

El programa debe funcionar para diferentes clientes, hasta que el usuario conteste que no desea procesar más clientes.

Para cada cliente se debe solicitar:

Su número de contrato, con siguiente formato (ddd-dddd) donde d es un número, por ejemplo (234-5241).
Potencia contratada.
El total de kW consumidos en el mes.
Realiza un programa que permita calcular el precio de la factura a cobrar, el cual viene dado por los siguientes datos:

El precio del kW es de 0.1684 kwh.
Según la potencia contratada,  se aplica una tarifa fija, según tabla:

Potencia    Precio

3,45 ---> 10,23 euros.
4,60 ---> 14,45 euros.
5,75 ---> 18,69 euros.
6,90 ---> 21,34 euros.
8,05 ---> 25,99 euros.

Adicionalmente, se realiza un incremento, el cual depende del total kW consumidos y viene dado en la siguiente tabla:   

     kW consumidos  
   Incremento   
0 - 150	 0 %
150 - 300	 5 %
300 - 400	 8 %
>400	 12 %

Utiliza las siguientes funciones:

Una función para pedir el número de contrato (validando posibles errores).
Una función para pedir la potencia contratada (validando posibles errores).
Una función para pedir los kW consumidos (validando posibles errores).
Una función para calcular el importe según los kW consumidos y la potencia contratada.
Una función para calcular el incremento.
Se desea hacer un informe con los siguientes datos por cliente:

Núm contrato
Total kW
Potencia
Incremento Precio a pagar
Total kW (todos los clientes) Facturado.
'''
import re
from utils import si_no


def pedir_contrato():
    contrato=True
    while contrato:
        contrato = input("Ingrese número de contrato (formato 123-4567): ")
        
        # Validaciones básicas
        if len(contrato) == 8 and contrato[3] == '-':
            parte1 = contrato[:3]
            parte2 = contrato[4:]
            
            if parte1.isdigit() and parte2.isdigit():
                contrato = False
    

def comprobar_formato():
    # ^Indica inicio de cadena, \d{3} tres digitos,
    # - guion,
    # \d{4} cuatro dígitos,
    #$ fin de cadena
    patron = r'^\d{3}-\d{4}$'
    return bool(re.match(patron, contrato))



def pedir_potencia():
    bucle=True
    tarifas_fijas = '''(1) 3,45 ---> 10,23 euros.
                       (2) 4,60 ---> 14,45 euros.
                       (3) 5,75 ---> 18,69 euros.
                       (4) 6,90 ---> 21,34 euros.
                       (5) 8,05 ---> 25,99 euros.
                    '''
    while bucle:
        print(f"Potencias disponibles: {(tarifas_fijas)}")
        potencia = int(input("Ingrese la potencia contratada: ")) 
        if potencia <= 5 and potencia > 0: 
            bucle=False
            if potencia == 1:
                potencia = 10.23
            elif potencia == 2:
                potencia = 14.45
            elif potencia == 3:
                potencia = 18.69
            elif potencia == 4:
                potencia = 21.34
            else:
                potencia = 25.99
        else:
            print("Potencia no válida. Elija una de la tabla seleccionando el numero como 1, 2, 3, 4 o 5")
    return potencia

def pedir_consumo():
    bucle = True
    while bucle:
        kw = int(input("Ingrese el total de kW consumidos en el mes: "))
        if kw >= 0:
            bucle= False
        else:
            print("El consumo no puede ser negativo.")
    return kw

def total_base(potencia, consumo):   
    precio_kw = 0.1684
    coste_consumo = consumo * precio_kw
    subtotal = potencia + coste_consumo
    return subtotal

def total_incremento(base):
    mult=0
    if base <= 150:
        mult = 0 # 0%
    elif 150 < base and base <= 300:
        mult = 0.05 # 5%
    elif 300 < base and base <= 400:
        mult = 0.08 # 8%
    else:
        mult = 0.12# 12% (> 400)
    return mult

def main():
    print("=== SISTEMA DE FACTURACIÓN ELÉCTRICA ===")
    
    # Acumuladores totales
    total_kw_global = 0
    total_facturado_global = 0
    
    procesar = True
    
    while procesar:
        print("\n=== Nuevo Cliente ===")
        
        # 1. Solicitar Datos
        contrato = pedir_contrato()
        potencia = pedir_potencia()
        consumo = pedir_consumo()

        # 2. Cálculos
        totalbase=total_base(potencia, consumo)
        incremento = total_incremento(consumo)
        totalincrem = totalbase * incremento
        precio_final = totalincrem + totalbase

        #Actualizar totales
        total_kw_global += consumo
        total_facturado_global += precio_final

        # 4. Mostrar Informe del Cliente
        print("\n" + "="*30)
        print(f"FACTURA CLIENTE: {contrato}")
        print("="*30)
        print(f"Potencia contratada:    {potencia} kW (Fijo: {potencia}€)")
        print(f"Total kW consumidos:    {consumo} kW")
        print(f"Importe Base:           {totalbase:.2f} €")
        print(f"Incremento aplicado:    {incremento*100:.0f}% ({totalincrem:.2f} €)")
        print("-" * 30)
        print(f"PRECIO A PAGAR:         {precio_final:.2f} €")
        print("="*30)
        
        # 5. Preguntar si continuar
        respuesta = si_no((f"Quiere continuar con un nuevo Cliente? (si/no): "))
        if respuesta != "si" and respuesta != "sí":
            procesar=False

    # Informe Final Global
    print("\n" + "*"*40)
    print("RESUMEN TOTAL DE LA JORNADA")
    print("*"*40)
    print(f"Total kW consumidos (todos los clientes): {total_kw_global:.2f} kW")
    print(f"Total Facturado (todos los clientes):     {total_facturado_global:.2f} €")

if __name__ == "__main__":
    main()
