from pystock.app.services.movements_service import *
from pystock.app.services.product_service import insert_product, drop_products
from pystock.app.services.sales_service import *


def before_each():
    insert_product("COD1", "NOMBRE1", "50", "")
    insert_product("COD2", "NOMBRE2", "150", "")
    insert_product("COD3", "NOMBRE3", "250", "")
    set_movement("COD1", 50, True)


def after_each():
    drop_collection()
    drop_products()
    drop_sales()


def test_insert_sale_with_one_product():
    before_each()
    client = "Marcelo"
    products = [{
        "cod": "COD1",
        "amount": "1"
    }]
    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1
    insert_sale(client, products)

    assert len(get_sales()[0]) == 1
    assert len(get_all_movements()) == 2

    first_sale = get_sales()[0][0]
    assert first_sale["client"] == client
    assert first_sale["products"] == products
    assert first_sale["price"] == 50

    after_each()


def test_insert_sale_with_two_products():
    before_each()
    set_movement("COD2", 50, True)
    client = "Marcelo"
    products = [
        {
            "cod": "COD1",
            "amount": "1"
        },
        {
            "cod": "COD2",
            "amount": "2"
        }
    ]
    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 2
    insert_sale(client, products)

    assert len(get_sales()[0]) == 1
    assert len(get_all_movements()) == 4

    first_sale = get_sales()[0][0]
    assert first_sale["client"] == client
    assert first_sale["products"] == products
    assert first_sale["price"] == 350

    after_each()


def test_insert_sale_with_stock_greater_than_available():
    before_each()
    client = "Marcelo"
    products = [{
        "cod": "COD1",
        "amount": "100"
    }]
    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1
    insert_sale(client, products)

    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1

    after_each()


def test_insert_sale_with_amount_zero():
    before_each()
    client = "Marcelo"
    products = [{
        "cod": "COD1",
        "amount": "0"
    }]
    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1
    insert_sale(client, products)

    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1

    after_each()


def test_insert_sale_with_negative_amount():
    before_each()
    client = "Marcelo"
    products = [{
        "cod": "COD1",
        "amount": "-10"
    }]
    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1
    insert_sale(client, products)

    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1

    after_each()


def test_insert_sale_with_same_product_multiple_times():
    before_each()
    client = "Marcelo"
    products = [
        {
            "cod": "COD1",
            "amount": "1"
        },
        {
            "cod": "COD1",
            "amount": "2"
        }
    ]
    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1
    insert_sale(client, products)

    assert len(get_sales()[0]) == 0
    assert len(get_all_movements()) == 1

    after_each()
