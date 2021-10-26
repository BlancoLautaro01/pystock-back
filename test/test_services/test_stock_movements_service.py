from pystock.app.services.stock_movements_service import *


def before_each():
    drop_collection()


def after_each():
    drop_collection()


def test_stock_movement():
    before_each()

    code = "COD001"
    quant = 10
    type_of_movement = True
    date = datetime.datetime.now()

    ret = insert_stock_movement(code, quant, type_of_movement, date)

    assert ret["id"] != None
    assert ret["cod"] == code
    assert ret["quantity"] == quant
    assert ret["type"] == type_of_movement
    assert ret["date"] == date

    after_each()


def test_get_stock_movement():
    before_each()

    code = "COD001"
    quant = 10
    type_of_movement = True
    date = str(datetime.datetime.now())

    insert_stock_movement(code, quant, type_of_movement, date)
    ret = get_stock_movement(code)


    assert ret["cod"] == code
    assert ret["quantity"] == quant
    assert ret["type"] == type_of_movement
    assert ret["date"] == date

    after_each()