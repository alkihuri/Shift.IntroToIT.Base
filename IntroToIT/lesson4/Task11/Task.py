#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
# Неправильное решение:
def wrong_sum_elements(lst):
    total = 0
    for i in lst:
        total += i
    return total