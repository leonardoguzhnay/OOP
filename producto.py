from pydantic import BaseModel, Field, ConfigDict, field_validator


class Producto(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    codigo: int = Field(..., gt=0)
    nombre: str = Field(..., min_length=3)
    precio: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        return value.title()

    @field_validator("precio")
    @classmethod
    def validar_precio(cls, value):
        if value <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        return value

    def mostrar_info(self):
        print("\n--- PRODUCTO ---")
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock: {self.stock}")


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