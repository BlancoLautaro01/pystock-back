from app.dao.user_mongo_dao import *


def before_each():
    drop_users()

def afeter_each():
    drop_users()

def test_user_exist():
    before_each()
    assert user_exist("luis@gmail.com") == False
    insert_user("luis@gmail.com","1234")
    assert user_exist("luis@gmail.com") == True
    afeter_each()

def test_insert_user():
    before_each()
    assert  user_exist("nomail@mail.com") == False
    insert_user("nomail@mail.com","1234")
    assert user_exist("nomail@mail.com") == True
    afeter_each()

def test_get_password():
    before_each()
    insert_user("nomail@mail.com","1234")
    assert get_password("nomail@mail.com") == "1234"
    afeter_each()

def test_get_id():
    before_each()
    insert_user("nomail@mail.com","1234")
    assert get_id("nomail@mail.com") is not None
    afeter_each()