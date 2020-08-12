import pymysql
import menu

"""connect - conecta ao DB
connection - var que contem a conecção
cursor - var que contem a execução"""
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="cadastro",
    charset="utf8mb4"
)


def conf_login(login, password):
    """Conferindo as informações para login no DB."""
    with connection.cursor() as cursor:
        select_login = f"select email, user from login where email = '{login}' or user = '{login}';"
        login_res = cursor.execute(select_login)#retorna 1-true, 0-false

        select_password = f"select password from login where email = '{login}' or user = '{login}' " \
                          f"and password = '{password}';"
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


def register(email, user, password):
    """Cadastrando um novo usuário"""
    with connection.cursor() as cursor:
        check_user_email = f"select email, user from login where email = '{email}' or user = '{user}';"
        res_check = cursor.execute(check_user_email)

        if res_check == 0:
            signing_up = f"insert into login values(default, '{email}', '{user}','{password}');"
            cursor.execute(signing_up)
            print("Cadastro efetuado com sucesso.")
            menu.interface_options()

        else:
            print("O usuário já existe.\nTente novamente")
            menu.register_user()

"""separar email e user para saber qual ja esta cadfastrado"""