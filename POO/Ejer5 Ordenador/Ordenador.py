class Ordenador:
    def __init__(self, ram, almacenamiento, procesador, pb, precio, tarjetaRed =True, grafica="Integrada", marca="Ninguna", modelo="Desconocido"):
        self.__grafica = grafica
        self.__marca = marca
        self.__modelo = modelo
        self.__ram = ram
        self.__almacenamiento = almacenamiento
        self.__procesador = procesador
        self.__placabase = pb
        self.__precio = precio
        self.__tarjetaRed = tarjetaRed
    
    def mostrarOrdenador(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, RAM: {self.__ram}GB, Almacenamiento: {self.__almacenamiento}GB, Procesador: {self.__procesador}, Placa base: {self.__placabase}, Precio: {self.calculaPrecio()}€, Grafica: {self.__grafica}, Tarjeta de red: {'Activada' if self.__tarjetaRed else 'Desactivada'}"

    def calculaPrecio(self):
        precio = self.get_precio()
        if self.isTarjetaRed():
            precio = precio + 80
        return precio

###############################
###     FUNCIONES SET       ###
###############################
    def set_precio(self, precio):
        self.__precio = precio

    def set_grafica(self, grafica):
        self.__grafica = grafica

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_ram(self, ram):
        self.__ram = ram

    def set_almacenamiento(self, almacenamiento):
        self.__almacenamiento = almacenamiento

    def set_procesador(self, procesador):
        self.__procesador = procesador

    def set_placabase(self, pb):
        self.__placabase = pb

    def set_tarjetaRed(self, tarjetaRed):
        self.__tarjetaRed = tarjetaRed


###############################
###     FUNCIONES GET       ###
###############################
    def get_precio(self):
        return self.__precio

    def get_grafica(self):
        return self.__grafica

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ram(self):
        return self.__ram

    def get_almacenamiento(self):
        return self.__almacenamiento

    def get_procesador(self):
        return self.__procesador

    def get_placabase(self):
        return self.__placabase

    def isTarjetaRed(self):
        return self.__tarjetaRed
