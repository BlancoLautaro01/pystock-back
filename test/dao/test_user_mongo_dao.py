from pystock.app.dao.user_mongo_dao import *


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


def test_insert_user_case_new_user():
    before_each()
    assert not user_exist("nomail@mail.com")
    insert_user("nomail@mail.com","1234")
    assert user_exist("nomail@mail.com")
    after_each()

def test_insert_user_case_allready_exist_user():
    before_each()
    assert not user_exist("nomail@mail.com")
    insert_user("nomail@mail.com","1234")
    assert user_exist("nomail@mail.com")
    insert_user("nomail@mail.com","otraContraseña")
    assert get_password("nomail@mail.com") == "1234"
    assert get_password("nomail@mail.com") != "otraContraseña"
    after_each()


def test_get_password():
    before_each()
    insert_user("nomail@mail.com","1234")
    assert get_password("nomail@mail.com") == "1234"
    after_each()


def test_get_users_case_no_users():
    before_each()
    assert len(get_users()) == 0
    after_each()

def test_get_users_case_3_users():
    before_each()
    users = []
    insert_user("email1@mail.com", "1234.1")

    users = get_users()
    assert len(users) == 1
    assert users[0]["email"] == "email1@mail.com"

    insert_user("email2@mail.com", "1234.2")
    users = get_users()
    assert len(users) == 2
    assert users[0]["email"] == "email1@mail.com"
    assert users[1]["email"] == "email2@mail.com"

    insert_user("email3@mail.com", "1234.3")
    users = get_users()
    assert len(users) == 3
    assert users[0]["email"] == "email1@mail.com"
    assert users[1]["email"] == "email2@mail.com"
    assert users[2]["email"] == "email3@mail.com"

    after_each()


def test_delete_user_case_user_exist():
    before_each()
    email = "warmi@gmail.com"

    assert not user_exist(email)

    insert_user(email, "1234")
    assert user_exist(email)

    delete_user(email)

    assert not user_exist(email)

    after_each()


def test_delete_user_case_user_not_exist():
    before_each()
    email = "warmi@gmail.com"

    assert not user_exist(email)

    delete_user(email)

    assert not user_exist(email)

    after_each()

"""
def test_get_id():
    before_each()
    insert_user("nomail@mail.com","1234")
    assert False
    after_each()"""
