class Producto:

    def __init__(self,nombre,precio,categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio>=0:
            self.precio = nuevo_precio
            return True
        raise ValueError("Producto no actualizado. Nuevo precio inválido")