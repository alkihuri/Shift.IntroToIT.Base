#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
# Неправильное решение:
def wrong_sum_elements(lst):
    total = 0
    for i in range(len(lst) - 1):
        total += lst[i]
    return total