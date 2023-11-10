#INTRO TO IT 2nd COURSE
# Задача: посчитать количество вхождений элемента в список
def count_occurrences(lst, element):
    count = 0
    for elem in lst:
        if elem == element:
            count += 1
    return count
