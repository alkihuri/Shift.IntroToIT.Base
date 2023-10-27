#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    return first_max + max(lst)