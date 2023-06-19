# Погружение в Python (семинары)
# Урок 10. ООП. Начало

import my_utils3 as mu3
import my_utils2 as mu2


if __name__ == '__main__':
    print('--== Тестирование класса MyCircle ==--')
    circle = mu3.MyCircle(5)
    print(f'Длина окружности радиусом {circle.radius} равна {circle.circle_len()=}')
    print(f'Площадь окружности радиусом {circle.radius} равна {circle.circle_square()=}')

    print('\n--== Тестирование класса MyRectangle ==--')
    rectangle = mu3.MyRectangle(5, 4)
    print(f'Периметр прямоугольника {rectangle.width}x{rectangle.height} равна {rectangle.rectangle_len()=}')
    print(f'Площадь прямоугольника {rectangle.width}x{rectangle.height} равна {rectangle.rectangle_square()=}')

    square = mu3.MyRectangle(8)
    print(f'Периметр квадрата {square.width}x{square.height} равна {square.rectangle_len()=}')
    print(f'Площадь квадрата {square.width}x{square.height} равна {square.rectangle_square()=}')

    print('\n--== Тестирование класса MyMan ==--')
    man = mu3.MyMan('Петр', 'Петров', 20)
    print(f'Полное имя: {man.fill_name()=}')
    print(f'Возраст: {man.get_age()=}')
    man.birthday()
    print(f'Возраст после дня рождения: {man.get_age()=}')
    man.__age = 40  # ошибки нет, но переменная __age не изменится
    print(f'Возраст после прямого изменения: {man.get_age()=}')

    print('\n--== Тестирование класса MyEmployee ==--')
    employee = mu3.MyEmployee('Василий', 'Пупкин', 35, employee_id=3001)
    print(f'Полное имя сотрудника: {employee.fill_name()}')
    print(f'Возраст сотрудника: {employee.get_age()}')
    man.birthday()
    print(f'Возраст после дня рождения сотрудника: {employee.get_age()=}')
    print(f'Возраст после дня рождения сотрудника: {employee.access_level()=}')

    print('\n--== Тестирование классов животных ==--')
    fish = mu3.MyFish('Карась', 10)
    bird = mu3.MyBird('Голубь', 100)
    creature = mu3.MyCreature('Бегемот', 300)
    print(f'Рыба {fish.name} плавает на глубине {fish.get_depth()} метров')
    print(f'Птица {bird.name} летает на высоте {bird.get_height()} метров')
    print(f'Зверь {creature.name} весит {creature.get_weight()} килограмм')

    print('\n--== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--')

    print('\n--== Тестирование общего класса животных ==--')
    animal_fish = mu3.AnyAnimal(mu3.MyFish('Щука', 20))
    print(f'Рыба {animal_fish.get_animal().name} плавает на глубине {animal_fish.get_animal().get_depth()} метров')
    animal_bird = mu3.AnyAnimal(mu3.MyBird('Синичка', 25))
    print(f'Птичка {animal_bird.get_animal().name} летает на высоте {animal_bird.get_animal().get_height()} метров')
    animal_creature = mu3.AnyAnimal(mu3.MyCreature('Кот', 19))
    print(f'Зверь {animal_creature.get_animal().name} весит {animal_creature.get_animal().get_weight()} килограмм')

    print('\n--== Тестирование математического модуля-класса ==--')
    quad_equat = mu2.QuadEquat(1, -1, -1)
    # Вычисляем корни одного уравнения
    print(quad_equat.get_pretty_string())

    # Вычисляем корни 100 случайных уравнений
    quad_equat.set_output_file('my_output.json', 100)
    quad_equat.get_roots_with_all_decorators()

# Результат работы:
# C:\Work\python\dz3\Py3HW10\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW10/main.py
# --== Тестирование класса MyCircle ==--
# Длина окружности радиусом 5 равна circle.circle_len()=31.41592653589793
# Площадь окружности радиусом 5 равна circle.circle_square()=78.53981633974483
#
# --== Тестирование класса MyRectangle ==--
# Периметр прямоугольника 5x4 равна rectangle.rectangle_len()=18
# Площадь прямоугольника 5x4 равна rectangle.rectangle_square()=20
# Периметр квадрата 8x8 равна square.rectangle_len()=32
# Площадь квадрата 8x8 равна square.rectangle_square()=64
#
# --== Тестирование класса MyMan ==--
# Полное имя: man.fill_name()='Петр Петров'
# Возраст: man.get_age()=20
# Возраст после дня рождения: man.get_age()=21
# Возраст после прямого изменения: man.get_age()=21
#
# --== Тестирование класса MyEmployee ==--
# Полное имя сотрудника: Василий Пупкин
# Возраст сотрудника: 35
# Возраст после дня рождения сотрудника: employee.get_age()=35
# Возраст после дня рождения сотрудника: employee.access_level()=5
#
# --== Тестирование классов животных ==--
# Рыба Карась плавает на глубине 10 метров
# Птица Голубь летает на высоте 100 метров
# Зверь Бегемот весит 300 килограмм
#
# --== ДОМАШНЕЕ ЗАДАНИЕ!!!! ==--
#
# --== Тестирование общего класса животных ==--
# Рыба Щука плавает на глубине 20 метров
# Птичка Синичка летает на высоте 25 метров
# Зверь Кот весит 19 килограмм
#
# --== Тестирование математического модуля-класса ==--
# Equation roots 1x^2 + -1x + -1: (-0.6180339887498949, 1.618033988749895)
#
# Process finished with exit code 0
