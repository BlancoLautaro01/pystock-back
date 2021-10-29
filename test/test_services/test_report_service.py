from pystock.app.services.movements_service import *
from pystock.app.services.product_service import insert_product, delete_product, get_by_cod
from pystock.app.services.report_service import get_report


def before_each():
    insert_product("COD1", "NOMBRE1", "", 50)
    insert_product("COD2", "NOMBRE2", "", 150)
    insert_product("COD3", "NOMBRE3", "", 250)


def after_each():
    drop_collection()


# def test_report():
#     set_movement("COD1", 10, True)
#     set_movement("COD1", "5", False)
#
#     set_movement("COD2", 10, True)
#
#     report = get_report()
#     assert not report
#     assert report[0] is not None