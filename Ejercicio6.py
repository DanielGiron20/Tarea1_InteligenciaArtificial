# Ejercicio 6: Fibonacci7
def fibonacci(n: int):
    # Verifica si n es menor o igual a 0
    if n <= 0:
        print("Por favor, ingrese un número mayor que 0.")
        return
    
    
    a, b = 0, 1
    
    #imprimir
    print("Secuencia de Fibonacci:")
    for i in range(n):
        print(a, end=", " if i < n - 1 else "\n")  # Imprime el número con formato
        a, b = b, a + b  
try:
    n = int(input("Ingrese el número de términos: "))
    fibonacci(n)
except ValueError:
    print("Por favor, ingrese un número válido.")
