from app.dao.user_mongo_dao import *


def before_each():
    drop_users()


def after_each():
    drop_users()


def test_user_exist():
    before_each()
    assert not user_exist("luis@gmail.com")
    insert_user("luis@gmail.com", "1234")
    assert user_exist("luis@gmail.com")
    after_each()


def test_insert_user():
    before_each()
    assert not user_exist("nomail@mail.com")
    insert_user("nomail@mail.com","1234")
    assert user_exist("nomail@mail.com")
    afeter_each()


def test_get_password():
    before_each()
    insert_user("nomail@mail.com","1234")
    assert get_password("nomail@mail.com") == "1234"
    after_each()


def test_get_id():
    before_each()
    insert_user("nomail@mail.com","1234")
    assert get_id("nomail@mail.com") is not None
    after_each()
