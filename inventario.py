class Inventario:

    def __init__(self):
        # LIST: mantiene los productos para mostrarlos ordenadamente
        self.productos = []

        # DICT: permite buscar rápidamente por código
        self.productos_por_codigo = {}

        # SET: evita registrar códigos duplicados
        self.codigos_registrados = set()

    def agregar_producto(self, producto):

        if producto.codigo in self.codigos_registrados:
            return False, "Ya existe un producto con ese código."

        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto
        self.codigos_registrados.add(producto.codigo)

        return True, "Producto agregado correctamente."

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, codigo):
        return self.productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo,
        nuevo_nombre,
        nuevo_precio,
        nuevo_stock
    ):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock

        return True, "Producto actualizado correctamente."

    def actualizar_stock(self, codigo, nuevo_stock):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        if nuevo_stock < 0:
            return False, "El stock no puede ser negativo."

        producto.stock = nuevo_stock
        return True, "Stock actualizado correctamente."

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)
        del self.productos_por_codigo[codigo]
        self.codigos_registrados.remove(codigo)

        return True, "Producto eliminado correctamente."