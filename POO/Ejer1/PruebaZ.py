def main():
    class Perro:
        def __init__(self,nombre,edad):
            self.nombre=nombre
            self.edad=edad
        def ladrar(self):
            print("Guau")
    
    perro1=Perro("Bobby",5)
    print(perro1.nombre)
    print(perro1.edad)
    perro1.ladrar()

    perro2=Perro("Firulais",3)
    print(perro2.nombre)
    print(perro2.edad)
    perro2.ladrar()

if __name__ == "__main__":
    main()
