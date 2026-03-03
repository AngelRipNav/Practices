
'''Ejercicio 4: Simulación de un sistema de pago con tarjeta
Estás desarrollando un sistema de pago para un comercio en línea. El sistema debe verificar si el saldo en la tarjeta de crédito es suficiente para realizar una compra. Si el saldo es mayor o igual al monto de la compra, el pago es aprobado. De lo contrario, debe rechazarse.

Instrucciones:

La función debe recibir el saldo de la tarjeta y el monto de la compra.
Si el saldo es suficiente, debe devolver el nuevo saldo.
Si el saldo no es suficiente, debe devolver el mismo saldo que tenia.
Programa principal, debe permitir hacer pagos hasta que la tarjeta se quede sin saldo (saldo=0).'''

from utils import *

def verificar_pago(saldo, monto_compra):
    """
    Verifica si el saldo es suficiente para realizar el pago.
    
    Args:
        saldo: Saldo actual de la tarjeta
        monto_compra: Monto de la compra a realizar
    
    Returns:
        El nuevo saldo si el pago es aprobado, o el saldo original si es rechazado
    """
    if saldo >= monto_compra:
        print(f"\nPago aprobado. Saldo anterior: {saldo}€")
        nuevo_saldo = saldo - monto_compra
        print(f"Monto pagado: {monto_compra}€")
        print(f"Nuevo saldo: {nuevo_saldo}€")
    else:
        print(f"\nPago rechazado. Saldo insuficiente.")
        print(f"Saldo disponible: {saldo}€")
        nuevo_saldo = saldo
        print(f"Monto requerido: {monto_compra}€")
    return nuevo_saldo

def main():
    print("=== SISTEMA DE PAGO CON TARJETA ===\n")
    
    # Solicitar saldo inicial
    saldo = float(input("Ingrese el saldo inicial de la tarjeta: "))
    
    # Continuar hasta que el saldo sea 0
    while saldo > 0:
        print(f"\n--- Saldo actual: {saldo}€ ---")
        monto_compra = float(input("Ingrese el monto de la compra (0 para salir): "))
        saldo = verificar_pago(saldo, monto_compra)
    
    if saldo == 0:
        print("\n¡La tarjeta se ha quedado sin saldo!")

if __name__ == "__main__":
    main()
