'''Ejercicio 3: Control de acceso a una zona restringida.
Estás desarrollando un sistema de control de acceso a una zona restringida. El sistema recibe una contraseña para permitir el acceso. Si la contraseña es correcta, el sistema debe permitir el acceso. Si es incorrecta, debe denegar el acceso. La contraseña correcta es "1234".

Instrucciones:

La función debe recibir una contraseña ingresada por el usuario.
Si la contraseña es "1234", debe devolver un mensaje indicando que el acceso fue concedido.
Si la contraseña es incorrecta, debe devolver un mensaje de denegación.
Programa principal: debe comprobar la contraseña hasta tener acceso.'''

from utils import *

def verificar_acceso(contrasena, contrasenas_validas):
    if contrasena in contrasenas_validas:
        acceso= "\nAcceso CONCEDIDO. Bienvenido a la zona restringida."
    else:
        acceso="\nAcceso DENEGADO. Contraseña incorrecta."
    return acceso

def main():
    # Lista de contraseñas válidas (usando lista como se solicita)
    contrasenas_validas = ["1234"]
    
    print("=" * 50)
    print("SISTEMA DE CONTROL DE ACCESO - ZONA RESTRINGIDA")
    print("=" * 50)
    
    acceso_concedido = False
    
    # Bucle hasta que se conceda el acceso
    while not acceso_concedido:
        contrasena = input("\nIngrese la contraseña de acceso: ")
        resultado = verificar_acceso(contrasena, contrasenas_validas)
        print(resultado)
        
        # Si la contraseña está en la lista de válidas, conceder acceso
        if contrasena in contrasenas_validas:
            acceso_concedido = True
    
    print("\n" + "=" * 50)
    print("Sesión iniciada correctamente.")
    print("=" * 50)

if __name__ == "__main__":
    main()
