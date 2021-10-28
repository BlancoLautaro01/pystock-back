from pystock.app.services.stock_service import *
from pystock.app.services.product_service import *

def before_each():
    drop_collection()
    drop_products()


def after_each():
    drop_collection()
    drop_products()

def test_insert_stock_case_good_response():
    before_each()

    code = "COD001"
    quant = 10
    insert_product(code, "name1", 100, "desc1")
    inserted_stock = insert_stock(code, quant)

    assert inserted_stock["cod"] == code
    assert inserted_stock["quantity"] == quant

    after_each()


def test_get_stock():
    before_each()

    code = "COD001"
    quant = 10
    insert_product(code, "name1", 100, "desc1")
    insert_stock(code, quant)
    inserted_stock = get_stock(code)

    assert inserted_stock["cod"] == code
    assert inserted_stock["quantity"] == quant

    after_each()


def test_update_stock_case_add_stock():
    before_each()

    code = "COD001"
    quant = 10
    stock_variation = 5

    insert_product(code, "name1", 100, "desc1")
    insert_stock(code, quant)

    update_stock(code, stock_variation, True)
    updated_stock = get_stock(code)

    assert updated_stock["cod"] == code
    assert updated_stock["quantity"] == quant + stock_variation

    after_each()


def test_update_stock_case_remove_stock():
    before_each()

    code = "COD001"
    quant = 10
    stock_variation = 5

    insert_product(code, "name1", 100, "desc1")
    insert_stock(code, quant)

    update_stock(code, stock_variation, False)
    updated_stock = get_stock(code)

    assert updated_stock["cod"] == code
    assert updated_stock["quantity"] == quant - stock_variation

    after_each()


def test_get_all_stock():
    before_each()

    insert_product("001", "name1", 101, "desc1")
    insert_product("002", "name2", 102, "desc2")
    insert_product("003", "name3", 103, "desc3")

    insert_stock("001", 1)
    insert_stock("002", 2)
    insert_stock("003", 3)

    stock = get_all_stock()

    assert stock[0]["cod"] == "001"
    assert stock[0]["name"] == "name1"
    assert stock[0]["quantity"] == 1

    assert stock[1]["cod"] == "002"
    assert stock[1]["name"] == "name2"
    assert stock[1]["quantity"] == 2

    assert stock[2]["cod"] == "003"
    assert stock[2]["name"] == "name3"
    assert stock[2]["quantity"] == 3

    after_each()
