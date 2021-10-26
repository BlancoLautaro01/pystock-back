from pystock.app.services.stock_service import *


def before_each():
    drop_collection()


def after_each():
    drop_collection()


def test_insert_stock_case_good_response():
    before_each()

    code = "COD001"
    quant = 10
    inserted_stock = insert_stock(code, quant)

    assert inserted_stock["cod"] == code
    assert inserted_stock["quantity"] == quant

    after_each()


def test_get_stock():
    before_each()

    code = "COD001"
    quant = 10
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

    insert_stock(code, quant)

    update_stock(code, stock_variation, False)
    updated_stock = get_stock(code)

    assert updated_stock["cod"] == code
    assert updated_stock["quantity"] == quant - stock_variation

    after_each()
