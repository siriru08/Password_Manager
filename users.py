
import storage

# Увеличеие id
def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


def reg(base):

    id_number = get_next_id(base)

    print("""
    ╔══════════════════════════════════════════════════╗
    ║                 Регистрация                      ║
    ╚══════════════════════════════════════════════════╝""")

    login_reg = input("    Введите Логин: ")
    password_reg = input("    Введите пароль: ")

    new_user = {
        "id": id_number,
        "name": login_reg,
        "password": password_reg
    }

    base.append(new_user)
    storage.save_contacts(base)

    return "    Аккаунт создан"

def biba():
    return "    Вход выполнен"



def login_users(base):
    while True:
        print("""
    ╔══════════════════════════════════════════════════╗
    ║                 Вход в аккаунт                   ║
    ╚══════════════════════════════════════════════════╝""")

        is_login = input("    Введите логин: ")
        is_password = input("    Введите пароль: ")


        for user in base:
            if (
                user["name"] == is_login
                and user["password"] == is_password
            ):
                return f"    Вход выполнен"


        print("    Ошибка: неверный логин или пароль")