class Livro:
    def __init__(self, titulo, autor, num_paginas, numeroexemplares=[]):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.disponivel = numeroexemplares

livro1 = Livro ("A menina que roubava livros", "Rafael","123")



