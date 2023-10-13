#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def f(s):
    return sum(1 for c in s if c.lower() in "аеёиоуыэюя")
s = "Привет, мир!"
print(f"В '{s}' {f(s)} гласных")
