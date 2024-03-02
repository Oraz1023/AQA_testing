def register_user(username, email, password, confirm_password):
    if not username:
        return "Введите имя пользователя"
    elif not email:
        return "Введите адрес электронной почты"
    elif '@' not in email or '.' not in email:
        return "Введите допустимый адрес электронной почты"
    elif len(password) < 6:  # Пусть минимальная длина пароля будет 6 символов
        return f"Пароль должен содержать не менее 6 символов"
    elif password != confirm_password:
        return "Пароли не совпадают"
    elif username in registered_users:
        return "Имя пользователя уже занято, выберите другое имя"
    elif not username.isalnum() or not password.isalnum():
        return "Имя пользователя и пароль могут содержать только буквы и цифры"
    elif not confirmation_type:
        return "Выберите способ подтверждения"
    elif email in registered_emails:
        return "Пользователь с таким адресом электронной почты уже зарегистрирован"
    else:
        # Здесь должен быть код для регистрации пользователя
        return "Пользователь успешно зарегистрирован"

# Примеры тестов:

registered_users = ["user1", "user2"]  # Список зарегистрированных пользователей
registered_emails = ["user1@example.com", "user2@example.com"]  # Список зарегистрированных адресов электронной почты
confirmation_type = "email"  # Тип подтверждения

# Тесты:

print(register_user("", "user@example.com", "password", "password"))  # Пустое имя пользователя
print(register_user("user", "", "password", "password"))  # Пустой адрес электронной почты
print(register_user("user", "userexample.com", "password", "password"))  # Недопустимый формат адреса электронной почты
print(register_user("user", "user@example.com", "pass", "pass"))  # Пароль короче минимальной длины
print(register_user("user", "user@example.com", "password", "pass"))  # Пароли не совпадают
print(register_user("user1", "user@example.com", "password", "password"))  # Имя пользователя уже занято
print(register_user("user!", "user@example.com", "password!", "password!"))  # Недопустимый символ в имени пользователя или пароле
print(register_user("user", "user@example.com", "password", "password"))  # Не выбран тип подтверждения
print(register_user("user", "user1@example.com", "password", "password"))  # Пользователь с таким адресом электронной почты уже зарегистрирован