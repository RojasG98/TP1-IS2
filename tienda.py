from producto import Producto

class Tienda:
    def __init__(self):
        self.inventario = []
    def agregar_producto(self, producto):
        self.inventario.append(producto)
    def buscar_producto(self,nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                return producto
        raise ValueError("Producto no encontrado")
        
    def eliminar_producto(self,nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                self.inventario.remove(producto)
                return True
        raise ValueError("Producto no eliminado")
    
    def actualizar_producto(self,nombre, nuevo_precio):
        if nuevo_precio>=0:
            for producto in self.inventario:
                if producto.nombre == nombre:
                    producto.precio = nuevo_precio
                    return True
        raise ValueError("Producto no actualizado")
    def aplicar_descuento(self,nombre, porcentaje):
        if 0 <= porcentaje <= 100:
            producto = self.buscar_producto(nombre)
            descuento = producto.precio * (porcentaje / 100)
            producto.precio -= descuento    
            return True
        else:
            raise ValueError("Porcentaje de descuento inválido")