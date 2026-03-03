
from Ordenador import *
from utils_v2 import *

def main():

    ram = pedir_num_extra(4, 128, "RAM")
    almacenamiento = pedir_num_extra(128, 4000, "Almacenamiento")
    procesador = pedir_texto("Procesador")
    placabase = pedir_texto("Placa base")
    precio = pedir_float(100, 10000, "Precio")
    grafica = input("Grafica: ")
    tarjetaRed = confirmar("Tiene tarjeta de red")
    marca = input("Marca: ")
    modelo = input("Modelo: ")

    ordenador1 = Ordenador(ram, almacenamiento, procesador, placabase, precio, tarjetaRed, grafica, marca, modelo)
    centrar_titulo("Ordenador 1")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_precio(1300)
    centrar_titulo("Ordenador 2")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_grafica("NVIDIA RTX 3060")
    centrar_titulo("Ordenador 3")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_marca("MSI")
    centrar_titulo("Ordenador 4")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_modelo("MSI MPG Z790 Carbon WiFi")
    centrar_titulo("Ordenador 5")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_ram(32)
    centrar_titulo("Ordenador 6")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_almacenamiento(1000)
    centrar_titulo("Ordenador 7")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_procesador("Intel Core i9")
    centrar_titulo("Ordenador 8")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_placabase("MSI Z790")
    centrar_titulo("Ordenador 9")
    print(f"{ordenador1.mostrarOrdenador()}")
    ordenador1.set_tarjetaRed(False)
    centrar_titulo("Ordenador 10")
    print(f"{ordenador1.mostrarOrdenador()}")

if __name__ == "__main__":
    main()
