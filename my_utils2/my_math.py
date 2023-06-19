"""
Математический модуль
Модуль не менял. Взял из прошлой домашней работы
"""


def find_roots(a, b, c):
    """
    Вычисление корней квадратного уравнения ax^2+bx+c=0
    :param a:
    :param b:
    :param c:
    :return: Корни уравнения, даже мнимые
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:  # мнимые корни
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        return (real_part, -imaginary_part), (real_part, imaginary_part)
    elif discriminant == 0:  # один действительный корень
        return -b / (2 * a)
    else:  # два действительных корня
        return ((-b - discriminant ** 0.5) / 2 * a,
                (-b + discriminant ** 0.5) / 2 * a,
                )
