import storage
import users

base = storage.load_contacts()

while True:
    is_login = input("""
    ╔══════════════════════════════════════════════════╗
    ║               PASSWORD MANAGER                   ║
    ╚══════════════════════════════════════════════════╝
    1. 🔐 Войти                     
    2. 📝 Регистрация
    3. 🚪 Выход   
    ────────────────────────────────────────────────────
    Выберите опцию: """)


    if is_login == "1":
        result = users.login_users(base)
        print(result)

    elif is_login == "2":
        print(users.reg(base))

    elif is_login == "3":
        break

