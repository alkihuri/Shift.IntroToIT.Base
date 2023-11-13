import unittest
from datetime import datetime 
from Task9.Task import *  
from Task10.Task import *  

class TestFunctions(unittest.TestCase):
 
    
    def test_reverse_string(self):
        # Тест на переворот строки
        # Строка 'abc' должна переворачиваться в 'cba'
        self.assertEqual(reverse_string('abc'), 'cba',
                         msg="Ошибка: строка перевернута неверно ('abc' != 'cba')")
    
    def test_factorial(self):
        # Тест на вычисление факториала
        # Факториал 5 должен быть 120
        self.assertEqual(factorial(5), 120,
                         msg="Ошибка: факториал рассчитан неверно (5! != 120)")

# Запуск тестов
if __name__ == '__main__':
    unittest.main()