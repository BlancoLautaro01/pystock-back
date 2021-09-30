import userMongoDAO as dao


def checkLogin(username, password):
    loginAcepted = False
    if dao.user_exist(username):
        result = dao.get_credentials(username)
        if password == result["password"]:
            loginAcepted = True
    return loginAcepted
