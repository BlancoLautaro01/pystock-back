from app.dao import user_mongo_dao as dao


def check_login(email, password):
    if dao.user_exist(email):
        pass_word = dao.get_password(email)
        return password == pass_word
    else:
        return False
