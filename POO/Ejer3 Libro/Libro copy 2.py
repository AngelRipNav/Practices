#codigo, titulo, formato, precio_alquiler definir tres metodos
from PruebaLibro import *

class Libro:
    def __init__(self, titulo, nombre_aut, nom_edit, ano_ed, isbn, precio, num_ej_tot, num_ej_prest):
        self.titulo=titulo
        self.nom_a = nombre_aut
        self.nom_ed = nom_edit
        self.ano = ano_ed
        self.isbn = isbn
        self.precio = precio
        self.num_ej_t = num_ej_tot
        self.num_ej_prest = num_ej_prest
    
    def mostrarLibro(self):
        centrar_titulo("Libro")
        print(f"\nEl titulo del libro es: {self.titulo}\n")
        print(f"El nombre del autor: {self.nom_a}\n")
        print(f"El nombre de la editorial: {self.nom_ed}\n")
        print(f"El año de edicion: {self.ano}\n")
        print(f"El ISBN: {self.isbn}\n")
        print(f"El precio: {self.precio}\n")
        print(f"El numero total de ejemplares: {self.num_ej_t}\n")
        print(f"El numero total de ejemplares prestados: {self.num_ej_prest}\n")

    def prestar(self):
        centrar_titulo("Prestar")
        if self.num_ej_prest < self.num_ej_t:
            print(f"El numero total de ejemplares prestados eran: {self.num_ej_prest}\n")
            self.num_ej_prest = self.num_ej_prest + 1
            print(f"El numero total de ejemplares prestados actualmente es: {self.num_ej_prest}\n")
        else:
            print(f"No se puede prestar. Todos los ejemplares ({self.num_ej_t}) ya estan prestados.\n")
    
    def devolver(self):
        centrar_titulo("Devolver")
        if self.num_ej_prest > 0:
            print(f"El numero total de ejemplares prestados eran: {self.num_ej_prest}\n")
            self.num_ej_prest = self.num_ej_prest - 1
            print(f"El numero total de ejemplares prestados actualmente es: {self.num_ej_prest}\n")
        else:
            print(f"No se puede devolver. No hay libros prestados para devolver")
