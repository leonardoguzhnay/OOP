from producto import (
    ProductoElectronico,
    ProductoAlimenticio
)

from inventario import Inventario
from pydantic import ValidationError


inventario = Inventario()


def agregar_producto():

    try:

        print("\nTIPO DE PRODUCTO")
        print("1. Electrónico")
        print("2. Alimenticio")

        tipo = input("Seleccione una opción: ")

        codigo = int(input("Código: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        if tipo == "1":

            producto = ProductoElectronico(
                codigo=codigo,
                nombre=nombre,
                precio=precio,
                stock=stock
            )

        elif tipo == "2":

            producto = ProductoAlimenticio(
                codigo=codigo,
                nombre=nombre,
                precio=precio,
                stock=stock
            )

        else:
            print("Tipo no válido.")
            return

        inventario.agregar_producto(producto)

    except ValidationError as e:

        print("\nError de validación:")
        print(e)

    except ValueError:

        print("\nIngrese datos válidos.")


def listar_productos():
    inventario.listar_productos()


def buscar_producto():

    codigo = int(input("Ingrese código del producto: "))

    producto = inventario.buscar_producto(codigo)

    if producto:
        producto.mostrar_info()
    else:
        print("Producto no encontrado.")


def actualizar_stock():

    codigo = int(input("Código del producto: "))
    nuevo_stock = int(input("Nuevo stock: "))

    inventario.actualizar_stock(codigo, nuevo_stock)


def eliminar_producto():

    codigo = int(input("Código del producto: "))

    inventario.eliminar_producto(codigo)


def menu():

    while True:

        print("\n==============================")
        print(" SISTEMA DE INVENTARIO")
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
            print("Opción inválida.")


if __name__ == "__main__":
    menu()