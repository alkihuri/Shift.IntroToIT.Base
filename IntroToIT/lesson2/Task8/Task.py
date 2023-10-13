#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def f(s):
    return len(s.split())
s = "Python прекрасен!"
print(f"В '{s}' {f(s)} слов")
