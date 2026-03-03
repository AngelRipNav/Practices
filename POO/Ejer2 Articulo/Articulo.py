#codigo, titulo, formato, precio_alquiler definir tres metodos

class Articulo:
    def __init__(self, codigo, titulo, formato, precio):
        self.formato = formato
        self.precio = precio
        self.titulo = titulo
        self.codigo = codigo

    def diaPrecio(self):
        return(self.precio)
    def dosPrecio(self):
        return(self.precio*2)
    def semanaPrecio(self):
        return(self.precio*7)
    def mostrarArticulo(self):
        print(f"\nEl codigo de la Pelicula es: {self.codigo}\n")
        print(f"El nombre de la Pelicula es: {self.titulo}\n")
        print(f"El formato de la Pelicula es: {self.formato}\n")
        print(f"El precio de alquilar la pelicula un dia seria: {self.diaPrecio()}$")
        print(f"El precio de alquilar la pelicula un dia seria: {self.dosPrecio()}$")
        print(f"El precio de alquilar la pelicula un dia seria: {self.semanaPrecio()}$")
