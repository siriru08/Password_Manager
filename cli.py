import storage

#новый пароль
def creation_pas(base):
    login = input("    Введите логин: ")
    password = input("    Введите пароль: ")
    site = input("    Введите ссылку на сайт: ")
    
    new_notion = {
        "login": login,
        "password": password,
        "site": site
    }
    
    base.append(new_notion)
    storage.save_contacts(base)
    
    
base = storage.load_contacts()
    
while True:
    main_site = input("""
    ╔══════════════════════════════════════════════════╗
    ║               PASSWORD MANAGER                   ║
    ╚══════════════════════════════════════════════════╝
    1. Добавить
    2. Изменить
    3. Просмотреть
    4. Удалить
    ────────────────────────────────────────────────────
    Выберите опцию: """)

    if main_site == '1':
        creation_pas(base)
    elif main_site == '2':
        pass
    elif main_site == '3':
        pass
    elif main_site == '4':
        pass
