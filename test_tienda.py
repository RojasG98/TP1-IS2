import pytest
from unittest.mock import Mock
from tienda import Tienda
from producto import Producto

@pytest.fixture
def tienda_con_productos():
    tienda = Tienda()
    tienda.agregar_producto(Producto("Queso", 5.50, "Lácteos"))
    tienda.agregar_producto(Producto("Huevos", 2.50, "Lácteos"))
    tienda.agregar_producto(Producto("Arroz", 1.00, "Granos"))
    tienda.agregar_producto(Producto("Leche", 0.99, "Lácteos"))
    tienda.agregar_producto(Producto("Pan", 1.20, "Panadería"))
    return tienda

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
    producto_encontrado = tienda_con_productos.buscar_producto("Pan")

    assert producto_encontrado is not None
    assert producto_encontrado.nombre == "Pan"
    assert producto_encontrado.precio == 1.20
    assert producto_encontrado.categoria == "Panadería"

def test_buscar_producto_no_existente():
    producto_encontrado = tienda_con_productos.buscar_producto("Jugo")

    assert producto_encontrado is None

def test_eliminar_producto_existente():
    resultado_eliminacion = tienda_con_productos.eliminar_producto("Huevos")

    assert resultado_eliminacion is True

def test_eliminar_producto_no_existente():
    resultado_eliminacion = tienda_con_productos.eliminar_producto("Yogur")

    assert resultado_eliminacion is False

def test_actualizar_producto_existente():

    resultado_actualizacion = tienda_con_productos.actualizar_producto("Arroz", 1.20)

    assert resultado_actualizacion is True
    producto_actualizado = tienda_con_productos.buscar_producto("Arroz")
    assert producto_actualizado.precio == 1.20

def test_actualizar_producto_no_existente():
    resultado_actualizacion = tienda_con_productos.actualizar_producto("Lentejas", 1.80)

    assert resultado_actualizacion is False

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

def test_aplicar_descuento_con_mock():
    tienda = Tienda()
    mock_producto = Mock()
    mock_producto.nombre = "Chocolate"
    mock_producto.precio = 2.00
    mock_producto.categoria = "Dulces"
    tienda.inventario = [mock_producto]
    tienda.aplicar_descuento("Chocolate", 10)
    
    mock_producto.actualizar_precio.assert_called_once_with(1.80)

