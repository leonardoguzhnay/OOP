from biblioteca import Biblioteca
from libro_impreso import LibroImpreso
from libro_digital import LibroDigital
from usuario import Usuario

# Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Crear materiales
libro1 = LibroImpreso(
    "L001",
    "Programación en Python",
    "Leonel Ribbeck",
    300
)

libro2 = LibroDigital(
    "D001",
    "POO Moderna",
    "Mario Torres",
    "PDF",
    30
)

# Crear usuario
usuario1 = Usuario(
    "0102030405",
    "Leonardo Guzhñay"
)

# Agregar a la biblioteca
biblioteca.agregar_material(libro1)
biblioteca.agregar_material(libro2)

biblioteca.agregar_usuario(usuario1)

# Mostrar información
biblioteca.mostrar_materiales()
biblioteca.mostrar_usuarios()