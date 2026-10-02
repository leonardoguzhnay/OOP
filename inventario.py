import json
from pathlib import Path

from producto import ProductoElectronico, ProductoAlimenticio


class Inventario:

    def __init__(self):
        # LIST: mantiene los productos para mostrarlos ordenadamente
        self.productos = []

        # DICT: permite buscar rápidamente por código
        self.productos_por_codigo = {}

        # SET: evita registrar códigos duplicados
        self.codigos_registrados = set()

        # Archivo JSON ubicado en la misma carpeta del proyecto
        self.archivo_datos = Path(__file__).parent / "productos.json"

        # Recupera automáticamente los datos guardados
        self.cargar_datos()

    # PERSISTENCIA DE DATOS

    def guardar_datos(self):
        """
        Convierte los productos en diccionarios y los guarda
        dentro del archivo productos.json.
        """

        datos = []

        for producto in self.productos:
            datos.append(
                {
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "precio": producto.precio,
                    "stock": producto.stock,
                    "tipo": producto.tipo,
                }
            )

        try:
            with open(
                self.archivo_datos,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4,
                )

            return True, "Datos guardados correctamente."

        except OSError as error:
            return False, f"No se pudieron guardar los datos: {error}"

    def cargar_datos(self):
        """
        Recupera los productos almacenados en productos.json
        cuando se inicia la aplicación.
        """

        if not self.archivo_datos.exists():
            return

        try:
            with open(
                self.archivo_datos,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

            for dato in datos:
                if dato["tipo"] == "Electrónico":
                    producto = ProductoElectronico(
                        int(dato["codigo"]),
                        dato["nombre"],
                        float(dato["precio"]),
                        int(dato["stock"]),
                    )
                elif dato["tipo"] == "Alimenticio":
                    producto = ProductoAlimenticio(
                        int(dato["codigo"]),
                        dato["nombre"],
                        float(dato["precio"]),
                        int(dato["stock"]),
                    )
                else:
                    continue

                # Se cargan directamente en las estructuras
                # para evitar guardar el archivo repetidamente
                self.productos.append(producto)

                self.productos_por_codigo[
                    producto.codigo
                ] = producto

                self.codigos_registrados.add(
                    producto.codigo
                )

        except json.JSONDecodeError:
            print(
                "El archivo productos.json está vacío "
                "o tiene un formato incorrecto."
            )

        except (OSError, KeyError, TypeError, ValueError) as error:
            print(f"Error al cargar los productos: {error}")

    # OPERACIONES CRUD

    def agregar_producto(self, producto):

        if producto.codigo in self.codigos_registrados:
            return False, "Ya existe un producto con ese código."

        self.productos.append(producto)

        self.productos_por_codigo[
            producto.codigo
        ] = producto

        self.codigos_registrados.add(
            producto.codigo
        )

        resultado, mensaje = self.guardar_datos()

        if not resultado:
            return False, mensaje

        return True, "Producto agregado y guardado correctamente."

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

        resultado, mensaje = self.guardar_datos()

        if not resultado:
            return False, mensaje

        return True, "Producto actualizado y guardado correctamente."

    def actualizar_stock(self, codigo, nuevo_stock):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        if nuevo_stock < 0:
            return False, "El stock no puede ser negativo."

        producto.stock = nuevo_stock

        resultado, mensaje = self.guardar_datos()

        if not resultado:
            return False, mensaje

        return True, "Stock actualizado y guardado correctamente."

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        self.productos.remove(producto)
        del self.productos_por_codigo[codigo]
        self.codigos_registrados.remove(codigo)

        resultado, mensaje = self.guardar_datos()

        if not resultado:
            return False, mensaje

        return True, "Producto eliminado correctamente."