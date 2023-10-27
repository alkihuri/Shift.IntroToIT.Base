#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 
# Неправильное решение:
def wrong_is_sorted(lst):
    return True if lst == sorted(lst, reverse=True) else False
