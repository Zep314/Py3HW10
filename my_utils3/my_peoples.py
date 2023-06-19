"""
Модуль содержит классы Человек и Сотрудник
"""


class MyMan:
    """
    Класс - человек.
    Содержит имя, фамилию, и возраст.
    Умеет "праздновать" день рождения
    """
    def __init__(self, first_name, last_name, age):
        self.__age = age  # Защищаем атрибут возраста
        self.first_name = first_name
        self.last_name = last_name

    def birthday(self):  # Праздник!!!
        self.__age += 1

    def get_age(self):
        return self.__age

    def fill_name(self):  # Выводим полное имя
        return f'{self.first_name} {self.last_name}'


class MyEmployee(MyMan):
    """
    Класс - Сотрудник. Наследуем от класса Человек
    """
    def __init__(self, *args, employee_id):
        super().__init__(*args)  # Передаем все параметры для класса Человек
        self.employee_id = employee_id  # У сотрудника есть свой ID, по которому определяем уровень доступа

    def access_level(self):  # Так определяем уровень доступа
        return self.employee_id % 7
