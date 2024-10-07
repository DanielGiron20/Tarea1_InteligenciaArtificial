import random
def adivina_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0  
    adivinado = False  
    
    print("¡Adivina el número entre 1 y 100!")
    while adivinado is False:
        try:
            intento = int(input("Ingresa tu intento: "))  
            intentos += 1  
            
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
            elif intento < numero_aleatorio:
                print("El número es mayor.")
            elif intento > numero_aleatorio:
                print("El número es menor.")
            else:
                print(f"¡Felicitaciones! Has adivinado el número en {intentos} intentos.")
                adivinado = True  
        except ValueError:
            print("Por favor, ingresa un número válido.")
adivina_numero()
