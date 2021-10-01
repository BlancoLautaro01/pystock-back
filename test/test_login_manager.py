import pytest
from app.user_mongo_dao import drop_users, insert_user
from app.login_manager import *

email = "luis@gmail.com"
password = "12345"

def before_each():
    drop_users()
    insert_user(email, password)

def afeter_each():
    drop_users()

def test_check_login_is_ok():
    before_each()
    assert check_login(email, password) == True
    afeter_each()

def test_check_login_is_not_ok_wrong_email():
    before_each()
    assert check_login("unEmailInexistente@gmail.com", password) == False
    afeter_each()

def test_check_login_is_not_ok_wrong_password():
    before_each()
    assert check_login(email, "1234") == False
    afeter_each()

