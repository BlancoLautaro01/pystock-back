from pystock.app.services.product_service import *


def before_each():
    drop_products()


def after_each():
    drop_products()


def test_product_exist():
    before_each()
    assert not product_exist("1")
    insert_product("1", "unNombreProducto", "precioProducto", "unaDescripcion")
    assert product_exist("1")
    after_each()


def test_insert_product():
    before_each()
    insert_product("COD1", "uNnombreProducto", "precioProducto", "unaDescripcion")
    assert product_exist("COD1")
    after_each()


def test_get_products_case_2_products():
    before_each()
    insert_product("COD1", "Pen", "Description 1", 50)

    products = get_products()
    assert len(products) == 1
    assert products[0]["cod"] == "COD1"

    insert_product("COD2", "Pecil", "Description 1", 50)
    products = get_products()
    assert len(products) == 2
    assert products[0]["cod"] == "COD1"
    assert products[1]["cod"] == "COD2"

    after_each()


def test_delete_product():
    before_each()
    product = insert_product("COD1", "uNnombreProducto", "precioProducto", "unaDescripcion")
    assert product_exist("COD1")
    delete_product(product["id"])
    assert not product_exist("COD1")
    after_each()
