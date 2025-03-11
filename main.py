class User:
    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
        self._access_level = 'user'

    def get_id(self):
        """Метод для получения ID пользователя"""
        return self.__id

    def get_name(self):
        """Метод для получения имени пользователя"""
        return self.__name

    def get_access_level(self):
        """Метод для получения уровня доступа пользователя"""
        return self._access_level

    def set_name(self, name):
        """Метод для изменения имени пользователя"""
        self.__name = name
        print(f'Пользователь ID={self.__id}, сменил имя на {self.__name}')
        return self

    def __str__(self):
        """magic methods"""
        return (f'{self.__name} (ID={self.__id}, Access_level={self._access_level})')


class Admin(User):
    __users = []

    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self._access_level = 'admin'
        self.__add_admin_to_users()

    def __add_admin_to_users(self) -> None:
        """Защищённый метод для добавления администратора в список"""
        if not any(user.get_id() == self.get_id() for user in Admin.__users):
            Admin.__users.append(self)
            print(f'Администратор {self.get_name()} успешно создан')

    def add_user(self, user: User):
        """Метод для добавления пользователя в список"""
        if isinstance(user, User):
            if user.get_id() in [u.get_id() for u in Admin.__users]:
                print(f'Не удалось создать пользователя {user.get_name()}. Пользователь с таким ID уже существует')
            else:
                Admin.__users.append(user)
                print(f'Пользователь {user.get_name()} успешно создан')
        else:
            print(f'Не удалось создать пользователя {user}. Можно добавлять только объекты User\n')

    def remove_user(self, user: User):
        """Метод для удаления пользователя из списка"""
        if isinstance(user, User):
            Admin.__users.remove(user)
            print(f'Пользователь {user.get_name()} удалён')
        else:
            print(f'Невозможно удалить {user}. Пользователь не найден')

    @classmethod
    def get_all_users(clc):
        return clc.__users.copy()


if __name__ == "__main__":
    admin = Admin(1, 'admin')
    admin2 = Admin(10, 'admin2')
    user1 = User(2, 'Вася')
    user2 = User(3, 'Петя')
    user3 = User(4, 'Коля')
    admin.add_user(user1)
    admin.add_user(user2)
    admin.add_user(user3)
    admin.add_user(User(2, 'Vasy'))
    admin.add_user('Petya')
    print(user3.get_access_level())

    print("Список пользователей:")
    for user in admin.get_all_users():
        print(user)

    admin.remove_user('Petya')
    admin.remove_user(user2)
    user3.set_name("Антон")

    print("Список пользователей:")
    for user in admin.get_all_users():
        print(user)
