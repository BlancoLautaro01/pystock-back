class Usuario:

    def __init__(self, usuario, contraseña):
        self._username = usuario
        self._password = contraseña

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, name):
        self._username = name

    @property
    def password(self):
        return self._password


def main():
    un_usuario = Usuario("jorge", "bokita")
    un_usuario.username = "carlitos"
    print(f"El usuario es {un_usuario.username} con contraseña {un_usuario.password}")


main()
