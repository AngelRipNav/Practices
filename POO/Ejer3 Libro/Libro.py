#codigo, titulo, formato, precio_alquiler definir tres metodos
from PruebaLibro import *

class Libro:
    def __init__(self, titulo, nombre_aut, nom_edit, ano_ed="Desconocido", isbn="Desconocido", precio="Desconocido", num_ej_tot="Desconocido", num_ej_prest="Desconocido"):
        self.__titulo=titulo
        self.__nombre_aut = nombre_aut
        self.__nom_edit = nom_edit
        self.__ano_ed = ano_ed
        self.__isbn = isbn
        self.__precio = precio
        self.__num_ej_tot = num_ej_tot
        self.__num_ej_prest = num_ej_prest

###############################
###     FUNCIONALIDADES     ###
###############################

    def mostrarLibro(self):
        centrar_titulo("Libro")
        return (f"\nEl titulo del libro es: {self.__titulo}\n\nEl nombre del autor: {self.__nombre_aut}\n\nEl nombre de la editorial: {self.__nom_edit}\n\nEl año de edicion: {self.__ano_ed}\n\nEl ISBN: {self.__isbn}\n\nEl precio: {self.__precio}\n\nEl numero total de ejemplares: {self.__num_ej_tot}\n\nEl numero total de ejemplares prestados: {self.__num_ej_prest}\n")
    
    def prestarLibro(self):
        prestado = True
        if self.__num_ej_prest < self.__num_ej_tot:
            self.__num_ej_prest+=1
        else:
            prestado = False
        return prestado
    
    def devolverLibro(self):
        devuelto = True
        if self.__num_ej_prest != 0:
            self.__num_ej_prest-=1
        else:
            devuelto = False
        return devuelto

###############################
###     FUNCIONES GET       ###
###############################

    def get_titulo(self):
        return self.__titulo
    
    def get_nombre_aut(self):
        return self.__nombre_aut
    
    def get_nom_edit(self):
        return self.__nom_edit
    
    def get_ano_ed(self):
        return self.__ano_ed
    
    def get_isbn(self):
        return self.__isbn
    
    def get_precio(self):
        return self.__precio
    
    def get_num_ej_tot(self):
        return self.__num_ej_tot
    
    def get_num_ej_prest(self):
        return self.__num_ej_prest

###############################
###     FUNCIONES SET       ###
###############################

    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def set_nombre_aut(self, nombre_aut):
        self.__nombre_aut = nombre_aut
    
    def set_nom_edit(self, nom_edit):
        self.__nom_edit = nom_edit
    
    def set_ano_ed(self, ano_ed):
        self.__ano_ed = ano_ed
    
    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def set_num_ej_tot(self, num_ej_tot):
        self.__num_ej_tot = num_ej_tot
    
    def set_num_ej_prest(self, num_ej_prest):
        self.__num_ej_prest = num_ej_prest

