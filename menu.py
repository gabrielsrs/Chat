from mysql import Mysql


def interface_options():
    print(f"{'Sistema de Login':^30}\n{'-' * 30}\n{'[1] Fazer login'}\n{'[2] Cadastrar-se'}\n{'-' * 30}")
    option = str(input("Escolha uma opção: "))
    print(f"{'-' * 30}")

    while True:
        if option != "1" and option != "2":
            print(f"Opção {option} não aceita. Tente novamente.")
            option = str(input("Escolha uma opção: "))
        else:
            if option == "1":
                return login()
            else:
                return register_user()


def login():
    user = str(input("Email ou usuário: "))
    password = str(input("Senha: "))
    response_enter = Mysql(login=user, password=password)
    response_enter.conf_login()

    return response_enter


def register_user():
    email = str(input("Digite seu email: ")).strip()
    user = str(input("Digite seu usuário: ")).strip()
    password = str(input("Digite sua senha: "))

    while True:
        if len(password) < 6:
            print("Senha tem que ter mais de 6 digitos.")
            password = str(input("Digite sua senha: "))
        else:
            break
    print(email, user)
    response_register = Mysql(email=email, user=user, password=password)
    response_register.register()
    return response_register
