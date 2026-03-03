class TrianguloEquilatero:
    def __init__(self, base, altura):
        self.base = base 
        self.altura=altura
    def perimetro(self):
        return 3 * self.base
    def area(self):
        return (self.base * self.altura) / 2

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base 
        self.altura=altura
    def perimetro(self):
        return 2 * (self.base + self.altura)
    def area(self):
        return self.base * self.altura

class Cuadrado:
    def __init__(self, base, altura):
        self.base = base 
        self.altura=altura
    def perimetro(self):
        return 4 * self.base
    def area(self):
        return self.base * self.altura

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def perimetro(self):
        return 2 * 3.1416 * self.radio
    def area(self):
        return 3.1416 * self.radio * self.radio
