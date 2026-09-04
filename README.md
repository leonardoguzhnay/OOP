# Sistema de Gestión de Inventario

## Descripción

Sistema desarrollado en Python que permite administrar productos dentro de un inventario mediante Programación Orientada a Objetos.

La aplicación permite registrar, consultar, actualizar y eliminar productos utilizando conceptos fundamentales de la programación como encapsulación, herencia, polimorfismo, composición y manejo de excepciones.

## Objetivo del Proyecto

Desarrollar una aplicación de consola para la gestión de productos en un inventario, aplicando los conceptos estudiados durante las primeras semanas de la asignatura de Programación Orientada a Objetos.

## Funcionalidades Principales

- Registrar productos.
- Buscar productos por código.
- Listar productos almacenados.
- Actualizar el stock de productos.
- Eliminar productos.
- Gestionar diferentes tipos de productos.
- Validar los datos ingresados por el usuario.
- Administrar el inventario mediante operaciones CRUD.

## Estructura del Proyecto

```text
proyecto-inventario/
│
├── main.py
├── producto.py
├── inventario.py
├── README.md
└── requirements.txt
```

## Clases Implementadas

### Clase Producto

Es la clase base del sistema.

Contiene los siguientes atributos:

- Código
- Nombre
- Precio
- Stock

Además, implementa encapsulación mediante atributos privados y métodos getters y setters para controlar el acceso a los datos.

### Clase ProductoElectronico

Hereda de la clase Producto.

Representa productos electrónicos y sobrescribe el método `mostrar_info()`, aplicando polimorfismo.

### Clase ProductoAlimenticio

Hereda de la clase Producto.

Representa productos alimenticios y sobrescribe el método `mostrar_info()`, aplicando polimorfismo.

### Clase Inventario

Administra todos los productos registrados en el sistema.

Implementa operaciones para:

- Agregar productos.
- Buscar productos.
- Listar productos.
- Actualizar stock.
- Eliminar productos.

La relación entre Inventario y Producto aplica el principio de composición, ya que un inventario está compuesto por múltiples productos.

## Conceptos de Programación Aplicados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

### Programación Orientada a Objetos

La solución se estructura mediante clases y objetos para representar entidades reales del sistema.

### Encapsulación

Se utilizaron atributos privados:

- `__codigo`
- `__nombre`
- `__precio`
- `__stock`

También se implementaron getters y setters mediante propiedades para controlar el acceso a los datos.

### Herencia

Las clases:

- ProductoElectronico
- ProductoAlimenticio

heredan atributos y métodos de la clase base Producto.

### Polimorfismo

Las clases derivadas sobrescriben el método:

```python
mostrar_info()
```

permitiendo diferentes comportamientos según el tipo de producto.

### Composición

La clase Inventario contiene una colección de objetos Producto para administrar el inventario.

### Manejo de Excepciones

Se utilizan bloques `try-except` para controlar errores durante el ingreso de datos por parte del usuario.

### CRUD

Se implementan las operaciones básicas:

- Crear productos.
- Consultar productos.
- Actualizar stock.
- Eliminar productos.

## Tecnologías Utilizadas

- Python 3
- Programación Orientada a Objetos (POO)

## Instalación

No se requieren librerías externas para ejecutar el proyecto.

## Ejecución

Ejecutar el programa mediante:

```bash
python main.py
```

## Ejemplo de Uso

1. Ejecutar el programa.
2. Seleccionar el tipo de producto.
3. Registrar la información.
4. Consultar los productos almacenados.
5. Actualizar el stock cuando sea necesario.
6. Eliminar registros del inventario.

## Conclusión

Este proyecto permite aplicar de forma práctica los conceptos fundamentales de Programación Orientada a Objetos, incluyendo clases, objetos, encapsulación, herencia, polimorfismo, composición y manejo de excepciones, mediante el desarrollo de un sistema funcional de gestión de inventario.

## Lenguaje Utilizado

Python

## Autor

Leonardo Guzhñay