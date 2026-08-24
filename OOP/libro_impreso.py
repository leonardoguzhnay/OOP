from material_bibliografico import MaterialBibliografico

class LibroImpreso(MaterialBibliografico):

    def __init__(self, codigo, titulo, autor, paginas):
        super().__init__(codigo, titulo, autor)
        self.__paginas = paginas

    def get_paginas(self):
        return self.__paginas

    def set_paginas(self, paginas):
        self.__paginas = paginas

    def mostrar_informacion(self):
        return (super().mostrar_informacion() +
                f" | Páginas: {self.__paginas}")