from pystock.app.dao import user_mongo_dao as dao


def check_login(email, password):
    if dao.user_exist(email):
        return password == dao.get_password(email)
    else:
        return False

