import user_mongo_dao as dao


def check_login(email, password):
    login_accepted = False
    if dao.user_exist(email):
        pass_word = dao.get_password(email)
        if password == pass_word:
            login_accepted = True
    return login_accepted
