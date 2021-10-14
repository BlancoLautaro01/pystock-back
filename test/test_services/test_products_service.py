from pystock.app.services.product_service import *


def before_each():
    drop_products()


def after_each():
    drop_products()


def test_product_exist():
    before_each()
    assert not product_exist("1")
    insert_product("1", "unombreProducto", "precioProducto", "UnaDescripcion")
    assert product_exist("1")
    after_each()

def test_insert_product():
    before_each()
    insert_product("1", "unombreProducto", "precioProducto", "UnaDescripcion")
    assert product_exist("1")
    after_each()

