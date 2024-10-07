class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, num_paginas: int):
        self.anio_publicacion = anio_publicacion
        self.autor = autor
        self.titulo = titulo
        self.num_paginas = num_paginas
    
    def mostrarInformacion(self):
        print("Informacion del libro")
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año de publicación:", self.anio_publicacion)
        print("Número de páginas:", self.num_paginas)

Milibro = Libro("Mas alla del bien y el mal", "Friedrich Nietzsche",1886 , 352)
Milibro.mostrarInformacion()