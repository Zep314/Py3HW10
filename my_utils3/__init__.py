"""
Init-файл для пакета с моими классами для 10-ого домашнего задания
"""

from my_utils3.my_geometry import MyCircle
from my_utils3.my_geometry import MyRectangle
from my_utils3.my_peoples import MyMan
from my_utils3.my_peoples import MyEmployee
from my_utils3.my_animals import MyFish
from my_utils3.my_animals import MyBird
from my_utils3.my_animals import MyCreature
from my_utils3.my_animals import AnyAnimal

# Эти классы будем "экспортировать" для внешней работы
__all__ = ['MyCircle', 'MyRectangle', 'MyMan', 'MyEmployee',
           'MyFish', 'MyBird', 'MyCreature', 'AnyAnimal']
