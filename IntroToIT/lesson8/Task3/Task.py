#INTRO TO IT 2nd COURSE
# Задача: вычислить факториал числа
def factorial(n):
    result = 1
    for i in range(2, n + 1):  # начальное значение интервала неправильное
        result *= i
    return result
