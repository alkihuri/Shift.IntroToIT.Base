import unittest
from datetime import datetime
from Task1.Task import add_numbers
from Task2.Task import days_until_birthday
from Task3.Task import calculate_salary
from Task4.Task import mortgage_payment
from Task5.Task import iphone_credit_cost 

class TestSumFunction(unittest.TestCase):   

    def test_add_numbers(self):
        result = add_numbers(3, 4)
        self.assertEqual(result, 7, msg=f"Тест 'add_numbers' не пройден. Результат = {result}")
        
    def test_days_until_birthday(self):
        result = days_until_birthday(datetime(2024, 12, 31))
        self.assertEqual(result, 65, msg=f"Тест 'days_until_birthday' не пройден. Результат = {result}")

    def test_calculate_salary(self):
        result = calculate_salary(10, 40)
        self.assertEqual(result, 400, msg=f"Тест 'calculate_salary' не пройден. Результат = {result}")

    def test_mortgage_payment(self):
        result = mortgage_payment(100000, 5, 30)
        self.assertAlmostEqual(result, 536.82, 2, msg=f"Тест 'mortgage_payment' не пройден. Результат = {result:.2f}")

    def test_iphone_credit_cost(self):
        result = iphone_credit_cost(1200, 24)
        self.assertEqual(result, 50, msg=f"Тест 'iphone_credit_cost' не пройден. Результат = {result}")


if __name__ == '__main__':
    unittest.main()
