#Ejercicio 10: 
import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        print("La longitud mínima de la contraseña debe ser 8 caracteres.")
        return
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    print(f"Contraseña generada: {contraseña}")

try:
    longitud = int(input("Ingrese la longitud deseada para la contraseña (mínimo 8): "))
    generar_contraseña(longitud)
except ValueError:
    print("Por favor, ingrese un número válido.")
