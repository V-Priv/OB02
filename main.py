
class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # функция getters для получения информации из защищенных аттрибутах
    def get_user_id(self): # запрос ID юзера
        return self._user_id

    def get_name(self): # запрос имени юзера
        return self._name

    def get_access_level(self): # запрос уровня доступа юзера
        return self._access_level

        # функция setters для изменения информации внутри защищенного аттрибута
    def set_name(self, name):
        self._name = name

    def set_access_level(self, level):  # Установка уровня доступа
        self._access_level = level

class Admin(User): # подкласс Admin обладает дополнительными методами(удаление и добавление в список, изменение прав доступа)
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._admin_access_level = 'admin'
        self._users_list = []

    # Методы для подкласа Admin
    def add_user(self, user): # метод добавления в список юзеров
        user_id = user.get_user_id()
        for existing_user in self._users_list:
            if existing_user.get_user_id() == user_id:
                print(f"Пользователь с ID {user_id} уже существует.")
                return

        self._users_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_id): # метод удаления из списка юзеров
        for user in self._users_list:
            if user.get_user_id() == user_id:
                self._users_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def change_user_access_level(self, user_id, new_level):  # Изменение уровня доступа юзера
        for user in self._users_list:
            if user.get_user_id() == user_id:
                user.set_access_level(new_level)
                print(f"Уровень доступа пользователя {user.get_name()} изменен на {new_level}.")
                return
        print(f"Пользователь с ID {user_id} не найден.")


    # Доступ к списку юзеров
    def get_users_list(self):
        return self._users_list

# Пример использования
admin = Admin(0, "Админ Иванов")
Петя = User(1, "Петр Петров")
Серый = User(2, "Сергей Сергеев")
user3 = User(3, "Павел Морозов")
user4 = User(4, "Андрей Исаев")
Кот = User(5,"Юрий Котов")


admin.add_user(Петя)
admin.add_user(Серый)
admin.add_user(user4)
admin.remove_user(2)
admin.add_user(Кот)
admin.change_user_access_level(5,"editor")
admin.change_user_access_level(4,"editor")



# Проверка списка пользователей
for user in admin.get_users_list():
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

