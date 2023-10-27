#INTRO TO IT 2nd COURSE
#Задача 8: Подсчет суммы цифр в числе
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))