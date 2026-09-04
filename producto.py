class Producto:

    def __init__(self, codigo, nombre, precio, stock):

        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # GETTERS

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    # SETTERS

    @nombre.setter
    def nombre(self, valor):

        if len(valor.strip()) >= 3:
            self.__nombre = valor

    @precio.setter
    def precio(self, valor):

        if valor > 0:
            self.__precio = valor

    @stock.setter
    def stock(self, valor):

        if valor >= 0:
            self.__stock = valor

    def mostrar_info(self):

        print("\n--- PRODUCTO ---")
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Stock: {self.__stock}")


class ProductoElectronico(Producto):

    def mostrar_info(self):

        print("\n--- PRODUCTO ELECTRÓNICO ---")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock: {self.stock}")


class ProductoAlimenticio(Producto):

    def mostrar_info(self):

        print("\n--- PRODUCTO ALIMENTICIO ---")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock: {self.stock}")