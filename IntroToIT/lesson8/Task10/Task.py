#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    first = second = float('-inf')
    for n in numbers:
        if n > first:
            first = n
        if n > second and n < first:
            second = n
    return second if second != float('-inf') else None

print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9
