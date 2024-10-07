class calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def multiplicacion(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 == 0:
            return("No se puede dividir entre 0")
        else:
            return self.num1 / self.num2

Suma = calculadora(5, 3)
Resta = calculadora(5, 3)
Multiplicacion = calculadora(5, 3)
Division = calculadora(5, 1)

print(Suma.suma())
print(Resta.resta())
print(Multiplicacion.multiplicacion())
print(Division.division())
    