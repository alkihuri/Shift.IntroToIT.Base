#INTRO TO IT 2nd COURSE
# Задача 7: Факториал на месте!
# Рассчитай факториал введенного числа.
def f(c):
    return 1 if c == 0 else c * f(c-1)
c = 5
print(f"Факториал {c} равен {f(c)}")
