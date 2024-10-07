def ContarVocales(cadena: str) -> int: #Nota se define la o las variables del metodo con su tipo de dato y se indica el tipo de dato que retorna
    vocales = ["a", "e", "i", "o", "u"]
    contador = 0
    for letra in cadena:
        if letra.lower() in vocales:
            contador += 1
    return contador

cadena = input("Introduce una cadena: ")
print(f"La cadena '{cadena}' tiene {ContarVocales(cadena)} vocales.")