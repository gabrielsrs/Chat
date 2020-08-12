import mysql


def interface_options():
    print(f"{'Sistema de Login':^30}\n{'-' * 30}\n{'[1] Fazer login'}\n{'[2] Cadastrar-se'}\n{'-' * 30}")
    option = str(input("Escolha uma opção: "))
    print(f"{'-' * 30}")

    while True:
        if "1" not in option and "2" not in option:
            print(f"Opção {option} não aceita. Tente novamente.")
            option = str(input("Escolha uma opção: "))
        else:
            break

    if option == "1":
        return login()
    else:
        return register_user()


def login():
    user = str(input("Email ou usuário: "))
    password = str(input("Senha: "))
    response_enter = mysql.conf_login(user, password)
    return response_enter


def register_user():
    email = str(input("Digite seu email: "))
    user = str(input("Digite seu usuário[opcional]: "))
    password = str(input("Digite sua senha: "))

    while True:
        if len(password) < 6:
            print("Senha tem que ter mais de 6 digitos.")
            password = str(input("Digite sua senha: "))
        else:
            break

    response_register = mysql.register(email, user, password)
    return response_register
