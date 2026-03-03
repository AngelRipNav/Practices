
class Perro:
    #Atributo de clase
    especie = "Canis lupus familiaris"
    #Inicializador
    def __init__(self, nombre, raza="No tiene"):
        print(f"Creando perro {nombre}, {raza}")
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    #Método de instancia
    def ladrar(self):
        print("Guau")
    
    def camina(self, pasos):
        print(f"Ha caminado {pasos} pasos")
