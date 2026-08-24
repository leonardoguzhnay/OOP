class Biblioteca:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__materiales = []
        self.__usuarios = []

    def agregar_material(self, material):
        self.__materiales.append(material)

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def mostrar_materiales(self):
        print("\n--- MATERIALES ---")
        for material in self.__materiales:
            print(material.mostrar_informacion())

    def mostrar_usuarios(self):
        print("\n--- USUARIOS ---")
        for usuario in self.__usuarios:
            print(usuario.mostrar_informacion())