"""
Модуль содержит классы для представления геометрических фигур
"""
from math import pi


class MyCircle:
    """
    Класс - окружность
    """
    def __init__(self, radius):
        self.radius = radius

    def circle_len(self) -> float:  # Длина окружности
        return 2 * pi * self.radius

    def circle_square(self) -> float:  # Площадь окружности
        return pi * self.radius ** 2


class MyRectangle:
    """
    Класс прямоугольник, который может быть квадратом
    """
    def __init__(self, *args):
        if len(args) == 1:  # Если один параметр - то это квадрат
            self.width = args[0]
            self.height = args[0]
        else:
            self.width = args[0]
            self.height = args[1]

    def rectangle_len(self):  # Периметр прямоугольника
        return 2 * (self.height + self.width)

    def rectangle_square(self):  # Площадь прямоугольника
        return self.height * self.width

