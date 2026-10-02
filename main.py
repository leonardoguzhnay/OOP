import flet as ft

from producto import ProductoElectronico, ProductoAlimenticio
from inventario import Inventario


inventario = Inventario()


def main(page: ft.Page):
    page.title = "Sistema de Inventario"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 25
    page.scroll = ft.ScrollMode.AUTO

    producto_seleccionado = {"codigo": None}

    # CAMPOS DE LA INTERFAZ

    tipo_producto = ft.Dropdown(
        label="Tipo de producto",
        width=250,
        options=[
            ft.dropdown.Option("Electrónico"),
            ft.dropdown.Option("Alimenticio"),
        ],
    )

    txt_codigo = ft.TextField(
        label="Código",
        width=200,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    txt_nombre = ft.TextField(
        label="Nombre del producto",
        width=300,
    )

    txt_precio = ft.TextField(
        label="Precio",
        width=200,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    txt_stock = ft.TextField(
        label="Stock",
        width=200,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    txt_buscar = ft.TextField(
        label="Código para buscar",
        width=220,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    mensaje = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.BOLD,
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Stock")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Seleccionar")),
        ],
        rows=[],
    )

    # FUNCIONES AUXILIARES

    def mostrar_mensaje(texto, es_error=False):
        mensaje.value = texto

        if es_error:
            mensaje.color = ft.Colors.RED
        else:
            mensaje.color = ft.Colors.GREEN

    def limpiar_campos(e=None):
        txt_codigo.value = ""
        txt_nombre.value = ""
        txt_precio.value = ""
        txt_stock.value = ""
        tipo_producto.value = None
        producto_seleccionado["codigo"] = None

        txt_codigo.disabled = False

        if e is not None:
            mostrar_mensaje("Campos limpiados correctamente.")

        page.update()

    def cargar_producto(producto):
        producto_seleccionado["codigo"] = producto.codigo

        txt_codigo.value = str(producto.codigo)
        txt_nombre.value = producto.nombre
        txt_precio.value = str(producto.precio)
        txt_stock.value = str(producto.stock)
        tipo_producto.value = producto.tipo

        # El código no se modifica porque identifica al producto
        txt_codigo.disabled = True

        mostrar_mensaje("Producto seleccionado correctamente.")
        page.update()

    def validar_campos():
        if not tipo_producto.value:
            raise ValueError("Seleccione un tipo de producto.")

        if not txt_codigo.value.strip():
            raise ValueError("Ingrese el código del producto.")

        if not txt_nombre.value.strip():
            raise ValueError("Ingrese el nombre del producto.")

        if not txt_precio.value.strip():
            raise ValueError("Ingrese el precio del producto.")

        if not txt_stock.value.strip():
            raise ValueError("Ingrese el stock del producto.")

        codigo = int(txt_codigo.value)
        nombre = txt_nombre.value.strip()

        precio_texto = txt_precio.value.strip().replace(",", ".")
        precio = float(precio_texto)

        stock = int(txt_stock.value)

        if codigo <= 0:
            raise ValueError("El código debe ser mayor que cero.")

        if len(nombre) < 3:
            raise ValueError("El nombre debe tener mínimo 3 caracteres.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        return codigo, nombre, precio, stock

    def actualizar_tabla():
        tabla.rows.clear()

        productos = inventario.listar_productos()

        for producto in productos:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(producto.codigo))),
                        ft.DataCell(ft.Text(producto.nombre)),
                        ft.DataCell(ft.Text(f"${producto.precio:.2f}")),
                        ft.DataCell(ft.Text(str(producto.stock))),
                        ft.DataCell(ft.Text(producto.tipo)),
                        ft.DataCell(
                            ft.IconButton(
                                icon=ft.Icons.EDIT,
                                tooltip="Seleccionar producto",
                                on_click=lambda e, p=producto: cargar_producto(p),
                            )
                        ),
                    ]
                )
            )

        page.update()

    # EVENTOS CRUD

    def agregar_producto(e):
        try:
            codigo, nombre, precio, stock = validar_campos()

            if tipo_producto.value == "Electrónico":
                producto = ProductoElectronico(
                    codigo,
                    nombre,
                    precio,
                    stock,
                )
            else:
                producto = ProductoAlimenticio(
                    codigo,
                    nombre,
                    precio,
                    stock,
                )

            resultado, texto = inventario.agregar_producto(producto)

            if resultado:
                limpiar_campos()
                actualizar_tabla()
                mostrar_mensaje(texto)
            else:
                mostrar_mensaje(texto, True)

        except ValueError as error:
            mostrar_mensaje(f"Error: {error}", True)

        except Exception as error:
            mostrar_mensaje(f"Ha ocurrido un error: {error}", True)

        page.update()

    def buscar_producto(e):
        try:
            if not txt_buscar.value.strip():
                raise ValueError("Ingrese un código para buscar.")

            codigo = int(txt_buscar.value)

            if codigo <= 0:
                raise ValueError("El código debe ser mayor que cero.")

            producto = inventario.buscar_producto(codigo)

            if producto is None:
                mostrar_mensaje("Producto no encontrado.", True)
                page.update()
                return

            cargar_producto(producto)
            mostrar_mensaje("Producto encontrado correctamente.")

        except ValueError as error:
            mostrar_mensaje(f"Error: {error}", True)

        except Exception as error:
            mostrar_mensaje(f"Ha ocurrido un error: {error}", True)

        page.update()

    def actualizar_producto(e):
        try:
            if producto_seleccionado["codigo"] is None:
                raise ValueError(
                    "Primero busque o seleccione un producto."
                )

            codigo = producto_seleccionado["codigo"]

            if not txt_nombre.value.strip():
                raise ValueError("Ingrese el nombre del producto.")

            if not txt_precio.value.strip():
                raise ValueError("Ingrese el precio del producto.")

            if not txt_stock.value.strip():
                raise ValueError("Ingrese el stock del producto.")

            nombre = txt_nombre.value.strip()
            precio = float(
                txt_precio.value.strip().replace(",", ".")
            )
            stock = int(txt_stock.value)

            if len(nombre) < 3:
                raise ValueError(
                    "El nombre debe tener mínimo 3 caracteres."
                )

            if precio <= 0:
                raise ValueError(
                    "El precio debe ser mayor que cero."
                )

            if stock < 0:
                raise ValueError(
                    "El stock no puede ser negativo."
                )

            resultado, texto = inventario.actualizar_producto(
                codigo,
                nombre,
                precio,
                stock,
            )

            if resultado:
                limpiar_campos()
                actualizar_tabla()
                mostrar_mensaje(texto)
            else:
                mostrar_mensaje(texto, True)

        except ValueError as error:
            mostrar_mensaje(f"Error: {error}", True)

        except Exception as error:
            mostrar_mensaje(f"Ha ocurrido un error: {error}", True)

        page.update()

    def eliminar_producto(e):
        try:
            codigo = producto_seleccionado["codigo"]

            if codigo is None:
                if not txt_codigo.value.strip():
                    raise ValueError(
                        "Primero busque o seleccione un producto."
                    )

                codigo = int(txt_codigo.value)

            resultado, texto = inventario.eliminar_producto(codigo)

            if resultado:
                limpiar_campos()
                actualizar_tabla()
                mostrar_mensaje(texto)
            else:
                mostrar_mensaje(texto, True)

        except ValueError as error:
            mostrar_mensaje(f"Error: {error}", True)

        except Exception as error:
            mostrar_mensaje(f"Ha ocurrido un error: {error}", True)

        page.update()

    # BOTONES

    btn_agregar = ft.ElevatedButton(
        text="Agregar",
        icon=ft.Icons.ADD,
        on_click=agregar_producto,
    )

    btn_buscar = ft.ElevatedButton(
        text="Buscar",
        icon=ft.Icons.SEARCH,
        on_click=buscar_producto,
    )

    btn_actualizar = ft.ElevatedButton(
        text="Actualizar",
        icon=ft.Icons.EDIT,
        on_click=actualizar_producto,
    )

    btn_eliminar = ft.ElevatedButton(
        text="Eliminar",
        icon=ft.Icons.DELETE,
        on_click=eliminar_producto,
    )

    btn_limpiar = ft.OutlinedButton(
        text="Limpiar",
        icon=ft.Icons.CLEAR,
        on_click=limpiar_campos,
    )

    # DISEÑO DE LA INTERFAZ

    formulario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Datos del producto",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                tipo_producto,
                ft.Row(
                    controls=[
                        txt_codigo,
                        txt_nombre,
                    ],
                    wrap=True,
                ),
                ft.Row(
                    controls=[
                        txt_precio,
                        txt_stock,
                    ],
                    wrap=True,
                ),
                ft.Row(
                    controls=[
                        btn_agregar,
                        btn_actualizar,
                        btn_eliminar,
                        btn_limpiar,
                    ],
                    wrap=True,
                ),
            ]
        ),
        padding=20,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
    )

    seccion_busqueda = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Buscar producto",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Row(
                    controls=[
                        txt_buscar,
                        btn_buscar,
                    ],
                    wrap=True,
                ),
            ]
        ),
        padding=20,
        border=ft.border.all(1, ft.Colors.GREY_300),
        border_radius=10,
    )

    page.add(
        ft.Text(
            "SISTEMA DE INVENTARIO",
            size=30,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Text(
            "Catálogo de productos electrónicos y alimenticios",
            size=16,
            color=ft.Colors.GREY_700,
        ),
        ft.Divider(),
        formulario,
        seccion_busqueda,
        mensaje,
        ft.Divider(),
        ft.Text(
            "Listado de productos",
            size=22,
            weight=ft.FontWeight.BOLD,
        ),
        ft.Row(
            controls=[tabla],
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    actualizar_tabla()


if __name__ == "__main__":
    ft.app(target=main)