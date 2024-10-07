# Ejercicio 1: Clase Rectángulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)
    
    # Crear una instancia de base 5 y altura 3
rectangulo = Rectangulo(5,3)
print("El area del rectangulo es: ",rectangulo.area())
print("El perimetro del rectangulo es: ",rectangulo.perimetro())



