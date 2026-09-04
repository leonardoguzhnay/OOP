from producto import ProductoElectronico
from producto import ProductoAlimenticio
from inventario import Inventario

inventario = Inventario()


def agregar_producto():

    try:

        print("\nTIPOS DE PRODUCTOS")
        print("1. Producto Electrónico")
        print("2. Producto Alimenticio")

        tipo = input("Seleccione una opción: ")

        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        if codigo <= 0:
            raise ValueError("El código debe ser mayor a cero.")

        if len(nombre.strip()) < 3:
            raise ValueError("El nombre debe tener mínimo 3 caracteres.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        if tipo == "1":
            producto = ProductoElectronico(
                codigo,
                nombre,
                precio,
                stock
            )
        elif tipo == "2":

            producto = ProductoAlimenticio(
                codigo,
                nombre,
                precio,
                stock
            )

        else:
            print("Tipo inválido.")
            return

        inventario.agregar_producto(producto)

    except ValueError as e:

        print(f"Error: {e}")


def listar_productos():

    inventario.listar_productos()


def buscar_producto():

    try:

        codigo = int(
            input("Ingrese el código del producto: ")
        )

        producto = inventario.buscar_producto(codigo)

        if producto:
            producto.mostrar_info()
        else:
            print("Producto no encontrado.")

    except ValueError:

        print("Ingrese un código válido.")


def actualizar_stock():

    try:

        codigo = int(
            input("Código del producto: ")
        )

        nuevo_stock = int(
            input("Nuevo stock: ")
        )

        inventario.actualizar_stock(
            codigo,
            nuevo_stock
        )

    except ValueError:

        print("Ingrese datos válidos.")


def eliminar_producto():

    try:

        codigo = int(
            input("Código del producto: ")
        )

        inventario.eliminar_producto(codigo)

    except ValueError:

        print("Ingrese un código válido.")


def menu():

    while True:

        print("\n==============================")
        print(" SISTEMA DE INVENTARIO ")
        print("==============================")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar stock")
        print("5. Eliminar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            agregar_producto()

        elif opcion == "2":

            listar_productos()

        elif opcion == "3":

            buscar_producto()

        elif opcion == "4":

            actualizar_stock()

        elif opcion == "5":

            eliminar_producto()

        elif opcion == "6":

            print("Programa finalizado.")
            break

        else:

            print("Opción no válida.")


if __name__ == "__main__":
    menu()