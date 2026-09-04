class Inventario:

    def __init__(self):

        # COMPOSICIÓN
        self.productos = []

    def agregar_producto(self, producto):

        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def listar_productos(self):

        if len(self.productos) == 0:
            print("No existen productos registrados.")
            return

        print("\n=== LISTADO DE PRODUCTOS ===")

        for producto in self.productos:
            producto.mostrar_info()

    def buscar_producto(self, codigo):

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_stock(self, codigo, nuevo_stock):

        producto = self.buscar_producto(codigo)

        if producto:
            producto.stock = nuevo_stock
            print("Stock actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(codigo)

        if producto:
            self.productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")