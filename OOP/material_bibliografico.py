class MaterialBibliografico:

    def __init__(self, codigo, titulo, autor):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_disponible(self):
        return self.__disponible

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.__disponible else "Prestado"

        return (f"Código: {self.__codigo} | "
                f"Título: {self.__titulo} | "
                f"Autor: {self.__autor} | "
                f"Estado: {estado}")