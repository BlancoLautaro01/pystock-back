from pystock.app.services.movements_service import *
from pystock.app.services.product_service import insert_product, drop_products
from pystock.app.services.report_service import get_report


def before_each():
    insert_product("COD1", "NOMBRE1", "50", "")
    insert_product("COD2", "NOMBRE2", "150", "")
    insert_product("COD3", "NOMBRE3", "250", "")


def after_each():
    drop_collection()
    drop_products()


def test_report():
    before_each()

    set_movement("COD1", 10, True)
    set_movement("COD1", "5", False)

    set_movement("COD2", 10, True)

    report = get_report()
    assert len(report) == 3
    assert report[0]["cod"] == "COD1"
    assert report[0]["total"] == 5

    assert report[1]["cod"] == "COD2"
    assert report[1]["total"] == 10

    assert report[2]["cod"] == "COD3"
    assert report[2]["total"] == 0

    after_each()
