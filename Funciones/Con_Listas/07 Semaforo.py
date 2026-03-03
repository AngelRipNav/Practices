'''Ejercicio 2: Simulación de un semáforo
Imagina que estás desarrollando una simulación de un semáforo en una ciudad. El semáforo cambia de color con el paso del tiempo. Necesitas escribir una función que reciba el color actual del semáforo (rojo, amarillo o verde) y devuelva el siguiente color.

Instrucciones:

La función debe recibir el color actual del semáforo como una cadena de texto.
El semáforo sigue el siguiente ciclo: Rojo → Verde → Amarillo → Rojo.
La función debe devolver el siguiente color del semáforo.
El programa principal debe ejecutar 5 ciclos del semáforo.'''

from utils import *

def siguiente_color(color_actual):

    #Devuelve el siguiente color del semáforo según el ciclo:
    #Rojo → Verde → Amarillo → Rojo y asin todo el rato
    if color_actual == "Rojo":
        color= "Verde"
    elif color_actual == "Verde":
        color= "Amarillo"
    elif color_actual == "Amarillo":
        color= "Rojo"
    return color
def main():
    print("===Semaforo ===\n")
    
    # Empezamos con el semáforo en Rojo
    color=siguiente_color(input("En que color esta el semaforo: "))
    print(f"Color inicial: {color}")
    # Ejecutar 5 ciclos del semáforo
    for ciclo in range(1, 6):
        color = siguiente_color(color)
        print(f"Ciclo {ciclo}: {color}")


if __name__ == "__main__":
    main()
