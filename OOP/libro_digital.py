from material_bibliografico import MaterialBibliografico

class LibroDigital(MaterialBibliografico):

    def __init__(self, codigo, titulo, autor, formato, tamanio_mb):
        super().__init__(codigo, titulo, autor)
        self.__formato = formato
        self.__tamanio_mb = tamanio_mb

    def get_formato(self):
        return self.__formato

    def get_tamanio_mb(self):
        return self.__tamanio_mb

    def set_formato(self, formato):
        self.__formato = formato

    def set_tamanio_mb(self, tamanio_mb):
        self.__tamanio_mb = tamanio_mb

    def mostrar_informacion(self):
        return (super().mostrar_informacion() +
                f" | Formato: {self.__formato}" +
                f" | Tamaño: {self.__tamanio_mb} MB")