#INTRO TO IT 2nd COURSE
def add_numbers(a, b):
    """
    Функция для сложения 2 чисел.
    :param a: Первое число
    :param b: Второе число
    :result: Сумма чисел
    """
    result = a + b
    return result

# Функция для умножения 2 чисел
def multiply_numbers(a, b):

    result = a * b
    return result

# Функция для нахождения максимального из списка
def find_max_number(numbers):

    max_number = max(numbers)
    return max_number

# Предупреждение: Этот код выводит не правильный результат при вводе отрицательных чисел
def calculate_factorial(n):

# TODO: Реализовать изключающее сообщение для отрицательных чисел
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Функция для проверки чётности числа
def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False

# Задаём 2 первичных числа
num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)

# Задаём список
numbers_list = [3, 8, 1, 6, 12]
max_num = find_max_number(numbers_list)

factorial_result = calculate_factorial(5)

is_even_num = is_even(7)

print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")