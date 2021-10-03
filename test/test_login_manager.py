from pystock.app.dao.user_mongo_dao import drop_users, insert_user
from pystock.app.login_manager import *

email = "luis@gmail.com"
password = "12345"


def before_each():
    drop_users()
    insert_user(email, password)


def after_each():
    drop_users()


def test_check_login_case_is_ok():
    before_each()
    assert check_login(email, password)
    after_each()


def test_check_login_case_is_not_ok_wrong_email():
    before_each()
    assert not check_login("unEmailInexistente@gmail.com", password)
    after_each()


def test_check_login_case_is_not_ok_wrong_password():
    before_each()
    assert not check_login(email, "1234")
    after_each()
