from producto import Producto

def test_creacion_producto():
    producto = Producto("Manzana", 0.50, "Frutas")
    assert producto.nombre == "Manzana"
    assert producto.precio == 0.50
    assert producto.categoria == "Frutas"