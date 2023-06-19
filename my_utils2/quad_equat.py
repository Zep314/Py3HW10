"""
Модуль содержит класс для решения квадратных уравнений, с генерацией случайных аргументов
и сохранением результатов в JSON файле
"""

from my_utils2.my_math import find_roots
from my_utils2.my_files import find_roots_with_all_decorators
from my_utils2.my_files import generate_csv


class QuadEquat:
    __output_file = 'output.json'  # Имя файла для результатов
    __amount = 100                 # Количество решаемых уравнений

    def __init__(self, a, b, c):  # Задаем параметры
        self.__a = a
        self.__b = b
        self.__c = c

    def get_roots(self):  # Решаем одно уравнение
        return find_roots(self.__a, self.__b, self.__c)

    def get_pretty_string(self):  # Красиво выводим результат решения
        return f'Equation roots {self.__a}x^2 + {self.__b}x + {self.__c}: {self.get_roots()}'

    def set_output_file(self, output_file, amount):  # Устанавливаем параметры для генерации случайных параметров
        self.__output_file = output_file
        self.__amount = amount

    def get_roots_with_all_decorators(self):  # Решаем случайные уравнения, сохраняем результат работы
        tmp_csv = 'tmp_input.csv'
        generate_csv(tmp_csv, self.__amount)
        find_roots_with_all_decorators(tmp_csv, self.__output_file)
