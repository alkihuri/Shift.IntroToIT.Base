import unittest
from datetime import datetime
from Task6.Task import *
from Task7.Task import *  
from Task8.Task import *    

class TestFunctions(unittest.TestCase):

    def test_fahrenheit_to_celsius(self):
        # Тест на проверку конвертации температуры
        # 32F -> 0C
        self.assertEqual(fahrenheit_to_celsius(32), 0, 
                         msg="Ошибка: конвертация температуры не верна (32F != 0C)")

    def test_heron_triangle_area(self):
        # Тест на площадь треугольника по формуле Герона
        # Для сторон 3, 4, 5 площадь должна быть 6
        self.assertEqual(heron_triangle_area(3, 4, 5), 6,
                         msg="Ошибка: площадь треугольника рассчитана неверно (3, 4, 5 != 6)")
    
    def test_sum_of_digits(self):
        # Тест на подсчет суммы цифр числа
        # Сумма цифр числа 123 должна быть 6
        self.assertEqual(sum_of_digits(123), 6,
                         msg="Ошибка: сумма цифр числа рассчитана неверно (123 != 6)")
     

# Запуск тестов
if __name__ == '__main__':
    unittest.main()