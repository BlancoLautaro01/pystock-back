from pystock.app.services.movements_service import *
from pystock.app.services.product_service import insert_product


def before_each():
    insert_product("COD1", "NOMBRE1", "", 50)
    insert_product("COD2", "NOMBRE2", "", 150)
    insert_product("COD3", "NOMBRE3", "", 250)


def after_each():
    drop_collection()


def test_set_movement():
    before_each()

    assert len(get_all_movements()) == 0
    movement_in = set_movement("COD1", 5, True)
    movement_out = set_movement("COD1", "5", False)

    assert not movement_in["id"] is None
    assert movement_in["cod"] == "COD1"
    assert movement_in["name"] == "NOMBRE1"
    assert movement_in["amount"] == 5
    assert movement_in["type"]
    assert not movement_in["date"] is None

    assert not movement_out["id"] is None
    assert movement_out["cod"] == "COD1"
    assert movement_out["name"] == "NOMBRE1"
    assert movement_out["amount"] == "5"
    assert not movement_out["type"]
    assert not movement_out["date"] is None

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


def test_set_movement_out_with_no_entry():
    before_each()

    movement = set_movement("COD1", 50, False)

    assert movement[0]["message"] == "ERROR: First movement of a product cant be 'out'"
    assert movement[1] == 500

    after_each()


def test_exists_movement_of():
    before_each()

    set_movement("COD1", 50, True)

    assert exists_movement_of("COD1")
    assert not exists_movement_of("COD2")

    after_each()
