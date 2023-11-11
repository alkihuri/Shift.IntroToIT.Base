#INTRO TO IT 2nd COURSE
# Задача: найти минимальное число в списке
def find_min(lst):
    if not lst:
        return None
    min_num = lst[0]
    for num in lst[1:]:
        if num > min_num:  # здесь условие должно быть на поиск минимума
            min_num = num
    return min_num