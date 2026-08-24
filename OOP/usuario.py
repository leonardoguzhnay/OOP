class Usuario:

    def __init__(self, identificacion, nombre):
        self.__identificacion = identificacion
        self.__nombre = nombre

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_informacion(self):
        return (f"ID: {self.__identificacion} | "
                f"Nombre: {self.__nombre}")