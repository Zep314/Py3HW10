"""
Модуль для работы с csv и json файлами
Модуль не менял. Взял из прошлой домашней работы
"""

import csv
import json
from random import randint
from my_utils2.my_math import find_roots

# Пределы коэффициентов уравнения
MIN_LIMIT = -100
MAX_LIMIT = 100
FILE_HEADER = ['A', 'B', 'C']


def generate_csv(filename, amount):
    """
    Функция генерирует csv файл с именем filename и amount строками
    Каждая строка - 3 случайных числа
    :param filename: Имя файла
    :param amount: Количество строк в файле
    :return:
    """
    if filename:
        with open(filename, 'w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=FILE_HEADER)
            writer.writeheader()
            writer.writerows([{'A': randint(MIN_LIMIT, MAX_LIMIT),
                               'B': randint(MIN_LIMIT, MAX_LIMIT),
                               'C': randint(MIN_LIMIT, MAX_LIMIT)} for _ in range(amount)]
                             )


def my_read_csv(filename):
    """
    Функция чтения информации из csv файла
    :param filename: Имя файла
    :return:
    """
    if filename:
        with open(filename, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            return [{k: int(v) for k, v in d.items()} for d in [row for row in reader]]


def quadratic_equation_decorator(func):
    """
    Декоратор - берет 3 значения из файла построчно, и вызывает декорируемую функцию с этими аргументами
    :param func:
    :return:
    """
    def wrapper(filename):
        with open(filename, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            ret = []
            for row in reader:  # Можно было оформить как dict comprehension, но тогда сильно непонятно становится
                a, b, c = map(int, row.values())
                result = func(a, b, c)  # Декорируемая функция
                ret.append({'A': a,
                            'B': b,
                            'C': c,
                            'text': f"Equation roots {a}x^2 + {b}x + {c}: {result}",
                            'result': result,
                            })
            return ret
    return wrapper


@quadratic_equation_decorator
def find_roots_with_deco(a, b, c):
    """
    Вычисление квадратного уравнения, с аргументами из csv файла
    :param a:
    :param b:
    :param c:
    :return:
    """
    return find_roots(a, b, c)


def save_to_json_decorator(func):
    """
    Сохранение результатов декорируемой функции в json-файл
    :param func:
    :return:
    """
    def wrapper(input_filename, output_filename):
        with open(output_filename, 'w', encoding='UTF-8') as f:
            data = func(input_filename)  # Декорируемая функция
            json.dump(data, f, indent=4)
    return wrapper


@save_to_json_decorator
def find_roots_with_2decos(input_file):
    """
    Вычисление корней квадратного уравнения, с аргументами из csv файла, и с сохранением результатов в json-файле
    :param input_file:
    :return:
    """
    return find_roots_with_deco(input_file)


@save_to_json_decorator
@quadratic_equation_decorator
def find_roots_with_all_decorators(a, b, c):
    """
    Вычисление корней квадратного уравнения, с аргументами из csv файла, и с сохранением результатов в json-файле
    Выполнено с применением 2-х декораторов сразу
    :param a:
    :param b:
    :param c:
    :return:
    """
    return find_roots(a, b, c)
