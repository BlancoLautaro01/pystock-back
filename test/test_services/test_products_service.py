import pytest

from pystock.app.services.product_service import *
from pystock.app.services.movements_service import set_movement, drop_collection



def before_each():
    drop_products()
    drop_collection()

def after_each():
    drop_products()
    drop_collection()

def test_product_exist():
    before_each()
    assert not product_exist("1")
    insert_product("1", "unNombreProducto", "200", "unaDescripcion")
    assert product_exist("1")
    after_each()


def test_insert_product():
    before_each()

    insert_product("COD1", "unNombreProducto", "200", "unaDescripcion")
    assert product_exist("COD1")

    after_each()


def test_update_product_success():
    before_each()

    product = insert_product("COD1", "unNombreProducto", "200", "unaDescripcion")
    update_product(product[0]["id"], "COD1", "Nombre Nuevo", "200", "unaDescripcion")

    edited_product = get_by_cod("COD1")
    assert edited_product["name"] == "Nombre Nuevo"

    after_each()


def test_update_product_cod_already_exist():
    before_each()

    product = insert_product("COD1", "unNombreProducto", "200", "unaDescripcion")
    insert_product("COD2", "uNnombreProducto", "200", "unaDescripcion")

    # El cod que se le esta queriendo editar al producto ya esta en uso por otro.
    response = update_product(product[0]["id"], "COD2", "Nombre Nuevo", "200", "unaDescripcion")

    # Por lo tanto no se edito.
    assert response[0]["message"] == "ERROR: Product with the same id already exists"
    assert product[0]["name"] == "unNombreProducto"
    assert product[0]["cod"] == "COD1"

    after_each()


def test_get_products_case_2_products():
    before_each()
    insert_product("COD1", "Pen", "50", "Description 1")

    products = get_products()
    assert len(products) == 1
    assert products[0]["cod"] == "COD1"

    insert_product("COD2", "Pecil", "50", "Description 1")
    products = get_products()
    assert len(products) == 2
    assert products[0]["cod"] == "COD1"
    assert products[1]["cod"] == "COD2"

    after_each()


def test_delete_product():
    before_each()
    product = insert_product("COD1", "unNombreProducto", "200", "unaDescripcion")
    assert product_exist("COD1")
    delete_product(product[0]["id"])
    assert not product_exist("COD1")
    after_each()


def test_get_products_with_stock():
    before_each()

    #preparacion
    cod1 = "cod001"
    cod2 = "cod011"
    cod3 = "cod563"
    producto1 = insert_product(cod1, "nombre1", 100, "desc1")
    producto2 = insert_product(cod2, "nombre2", 100, "desc2")
    producto3 = insert_product(cod3, "nombre3", 100, "desc3")

    #ingreso stock para los 3 productos
    set_movement(cod1, 100, True)
    set_movement(cod2, 100, True)
    set_movement(cod3, 100, True)

    #saco stock para para vaciar el stock de 1 producto, dejar parcialmente vacio otro
    set_movement(cod1, 100, False)
    set_movement(cod2, 50, False)
    set_movement(cod3, 1, True)

    productos_con_stock = []
    productos_con_stock.append(producto1)
    productos_con_stock.append(producto2)

    assert len(productos_con_stock) == 2
    assert not producto1 in productos_con_stock
    assert producto2 in productos_con_stock
    assert producto3 in productos_con_stock

    after_each()
