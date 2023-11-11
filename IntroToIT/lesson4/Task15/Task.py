#INTRO TO IT 2nd COURSE

# Задача 15: Подсчитать количество четных чисел в списке.
# Правильное решение:
def correct_count_even(lst):
    return len([x for x in lst if x % 2 == 0])

# Неправильное решение:
def wrong_count_even(lst):
    count = 0
    for num in lst:
        if not num % 2:
            count += 1
        else:
            count -= 1
    return count