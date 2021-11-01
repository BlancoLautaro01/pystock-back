from pystock.app.services.movements_service import *
from pystock.app.services.product_service import insert_product


def before_each():
    drop_collection()
    insert_product("COD1", "NOMBRE1", "50", "")
    insert_product("COD2", "NOMBRE2", "150", "")
    insert_product("COD3", "NOMBRE3", "250", "")


def after_each():
    drop_collection()


def test_set_movement():
    before_each()

    assert len(get_all_movements()) == 0
    movement_in = set_movement("COD1", 5, True)
    movement_out = set_movement("COD1", "5", False)

    assert not movement_in[0]["id"] is None
    assert movement_in[0]["cod"] == "COD1"
    assert movement_in[0]["name"] == "NOMBRE1"
    assert movement_in[0]["amount"] == 5
    assert movement_in[0]["type"]
    assert not movement_in[0]["date"] is None

    assert not movement_out[0]["id"] is None
    assert movement_out[0]["cod"] == "COD1"
    assert movement_out[0]["name"] == "NOMBRE1"
    assert movement_out[0]["amount"] == 5
    assert not movement_out[0]["type"]
    assert not movement_out[0]["date"] is None

    assert len(get_all_movements()) == 2

    after_each()


def test_set_movement_string_amount():
    before_each()

    movement = set_movement("COD1", "amount", True)

    assert movement[0]["message"] == "ERROR: Quantity field can only be numbers"
    assert movement[1] == 500

    after_each()


def test_set_movement_unexisting_product_cod():
    before_each()

    movement = set_movement("RandomCode", 50, True)

    assert movement[0]["message"] == "ERROR: Product code not exists"
    assert movement[1] == 500

    after_each()


def test_set_movement_amount_less_than_one():
    before_each()

    movement0 = set_movement("COD1", 0, True)
    movement_minus_0 = set_movement("COD1", -10, True)

    assert movement0[0]["message"] == "ERROR: Amount cant be less than 1"
    assert movement0[1] == 500

    assert movement_minus_0[0]["message"] == "ERROR: Amount cant be less than 1"
    assert movement_minus_0[1] == 500

    after_each()


def test_set_movement_out_leaving_negative_stock():
    before_each()

    movement = set_movement("COD1", 10, False)

    assert movement[0]["message"] == "ERROR: Out movement cant leave a negative product stock"
    assert movement[1] == 500

    set_movement("COD1", 10, True)
    movement = set_movement("COD1", 15, False)

    assert movement[0]["message"] == "ERROR: Out movement cant leave a negative product stock"
    assert movement[1] == 500

    movement = set_movement("COD1", 5, False)

    assert movement[0]["cod"] == "COD1"

    after_each()


def test_exists_movement_of():
    before_each()

    set_movement("COD1", 50, True)

    assert exists_movement_of("COD1")
    assert not exists_movement_of("COD2")

    after_each()


def test_delete_movement():
    before_each()

    movement = set_movement("COD1", 50, True)
    assert exists_movement_of("COD1")

    delete_movement(movement[0]["id"])
    assert not exists_movement_of("COD1")

    after_each()
