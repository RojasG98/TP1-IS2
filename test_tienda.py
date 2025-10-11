import pytest
from tienda import Tienda
from producto import Producto

def test_crear_tienda_inicial():
    tienda = Tienda()
    assert tienda.inventario == []

def test_agregar_producto_y_verificar_inventario():
    tienda = Tienda()
    producto_nuevo = Producto("Queso", 5.50, "Lácteos")

    tienda.agregar_producto(producto_nuevo)

    assert len(tienda.inventario) == 1
    assert tienda.inventario[0].nombre == "Queso"
    assert tienda.inventario[0].precio == 5.50
    assert tienda.inventario[0].categoria == "Lácteos"

def test_buscar_producto_existente():
    tienda = Tienda()
    producto_nuevo = Producto("Pan", 1.20, "Panadería")
    tienda.agregar_producto(producto_nuevo)

    producto_encontrado = tienda.buscar_producto("Pan")

    assert producto_encontrado is not None
    assert producto_encontrado.nombre == "Pan"
    assert producto_encontrado.precio == 1.20
    assert producto_encontrado.categoria == "Panadería"

def test_buscar_producto_no_existente():
    tienda = Tienda()
    producto_nuevo = Producto("Leche", 0.99, "Lácteos")
    tienda.agregar_producto(producto_nuevo)

    producto_encontrado = tienda.buscar_producto("Jugo")

    assert producto_encontrado is None

def test_eliminar_producto_existente():
    tienda = Tienda()
    producto_nuevo = Producto("Huevos", 2.50, "Lácteos")
    tienda.agregar_producto(producto_nuevo)

    resultado_eliminacion = tienda.eliminar_producto("Huevos")

    assert resultado_eliminacion is True
    assert len(tienda.inventario) == 0

def test_eliminar_producto_no_existente():
    tienda = Tienda()
    producto_nuevo = Producto("Cereal", 3.75, "Desayuno")
    tienda.agregar_producto(producto_nuevo)

    resultado_eliminacion = tienda.eliminar_producto("Yogur")

    assert resultado_eliminacion is False
    assert len(tienda.inventario) == 1

def test_actualizar_producto_existente():
    tienda = Tienda()
    producto_nuevo = Producto("Arroz", 1.00, "Granos")
    tienda.agregar_producto(producto_nuevo)

    resultado_actualizacion = tienda.actualizar_producto("Arroz", 1.20)

    assert resultado_actualizacion is True
    producto_actualizado = tienda.buscar_producto("Arroz")
    assert producto_actualizado.precio == 1.20

def test_actualizar_producto_no_existente():
    tienda = Tienda()
    producto_nuevo = Producto("Frijoles", 1.50, "Granos")
    tienda.agregar_producto(producto_nuevo)

    resultado_actualizacion = tienda.actualizar_producto("Lentejas", 1.80)

    assert resultado_actualizacion is False
    producto_no_actualizado = tienda.buscar_producto("Frijoles")
    assert producto_no_actualizado.precio == 1.50

def test_excepcion_en_buscar_producto():
    tienda = Tienda()
    with pytest.raises(ValueError):
        tienda.buscar_producto("NoExiste") 

def test_excepcion_en_eliminar_producto():
    tienda = Tienda()
    with pytest.raises(ValueError):
        tienda.eliminar_producto("NoExiste")

def test_excepcion_en_actualizar_producto():
    tienda = Tienda()
    with pytest.raises(ValueError):
        tienda.actualizar_producto("NoExiste", 10.0)

