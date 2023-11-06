#INTRO TO IT 2nd COURSE
# Задача 9: Переворот строки
def reverse_string(s):
    return ''.join(sorted(s, reverse=True))