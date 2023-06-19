"""
Модуль содержит классы разных животных, и общий, универсальный класс для работы с разными животными
"""


class MyAnimal:
    """
    Общий, универсальный класс для всех животных
    """
    def __init__(self, name):
        self.name = name


class MyFish(MyAnimal):
    """
    Класс - рыб.
    Храним насколько глубоко рыба умеет плавать
    """
    def __init__(self, name, depth):
        super().__init__(name)
        self.__depth = depth

    def get_depth(self):
        return self.__depth


class MyBird(MyAnimal):
    """
    Класс - птиц.
    Храним насколько высоко птица умеет летать
    """
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    def get_height(self):
        return self.__height


class MyCreature(MyAnimal):
    """
    Класс - млекопитающих.
    Храним насколько тяжелое млекопитающее
    """

    def __init__(self, name, weight):
        super().__init__(name)
        self.__weight = weight

    def get_weight(self):
        return self.__weight


class AnyAnimal:
    """
    Класс - животное. Храним экземпляр любого класса - наследника Animal
    """
    def __init__(self, animal):
        self.animal = animal

    def get_animal(self):  # Возвращаем экземпляр класса - наследника от Animal
        return self.animal
