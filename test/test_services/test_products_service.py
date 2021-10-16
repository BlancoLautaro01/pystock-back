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

    insert_product("COD1", "unNombreProducto", "precioProducto", "unaDescripcion")
    assert product_exist("COD1")

    after_each()


def test_update_product_success():
    before_each()

    product = insert_product("COD1", "unNombreProducto", "precioProducto", "unaDescripcion")
    update_product(product["id"], "COD1", "Nombre Nuevo", "precioProducto", "unaDescripcion")

    edited_product = get_by_cod("COD1")
    assert edited_product["name"] == "Nombre Nuevo"

    after_each()


def test_update_product_cod_already_exist():
    before_each()

    product = insert_product("COD1", "unNombreProducto", "precioProducto", "unaDescripcion")
    insert_product("COD2", "uNnombreProducto", "precioProducto", "unaDescripcion")

    # El cod que se le esta queriendo editar al producto ya esta en uso por otro.
    update_product(product["id"], "COD2", "Nombre Nuevo", "precioProducto", "unaDescripcion")

    # Por lo tanto no se edito.
    assert product["name"] == "unNombreProducto"
    assert product["cod"] == "COD1"

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
    product = insert_product("COD1", "unNombreProducto", "precioProducto", "unaDescripcion")
    assert product_exist("COD1")
    delete_product(product["id"])
    assert not product_exist("COD1")
    after_each()
