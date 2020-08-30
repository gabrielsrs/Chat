class Mysql:
    import pymysql

    connection = pymysql.connect(host="localhost", user="root", password="", db="cadastro", charset="utf8mb4")

    def __init__(self, email="", user="", login="", password=""):
        self.email = email
        self.user = user
        self.login = login
        self.password = password

    def conf_login(self):
        """Conferindo as informações para login no DB."""
        with self.connection.cursor() as cursor:
            select_login = f"select email, user from login where email = '{self.login}' or user = '{self.login}';"
            login_res = cursor.execute(select_login)#retorna 1-true, 0-false

            select_password = f"select password from login where email = '{self.login}' or user = '{self.login}' " \
                              f"and password = '{self.password}';"
            login_password = cursor.execute(select_password)

        if login_res == 1 and login_password == 1:
            print(f"{'-' * 30}")
            print("Login efetuado com sucesso.")
            print(f"{'-' * 30}")

        else:
            print(f"{'-' * 30}")
            print("Falha ao efetuar o login.\nTente novamente.")
            print(f"{'-' * 30}")
            menu.interface_options()

    def register(self):
        """Cadastrando um novo usuário"""
        with self.connection.cursor() as cursor:
            check_user_email = f"select email, user from login where email = '{self.email}' or user = '{self.user}';"
            res_check = cursor.execute(check_user_email)

            if res_check == 0:
                signing_up = f"insert into login values(default, '{self.email}', '{self.user}','{self.password}');"
                cursor.execute(signing_up)
                print("Cadastro efetuado com sucesso.")
                menu.interface_options()

            else:
                print("Erro de cadastro.\nTente novamente")
                menu.register_user()
