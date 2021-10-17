from pystock.app.services import user_service as dao


def check_login(email, password):
    if dao.user_exist(email):
        return password == dao.get_password(email)
    else:
        return False
