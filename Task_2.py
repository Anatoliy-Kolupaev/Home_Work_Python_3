# Задача № 2
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import math
import random

n = int(input('Введите кол-во элементов: '))
l = [random.randint(1, 10) for i in range(n)]
print(l)


def Result(l):
    a = []
    for i in range(math.ceil(len(l)/2)):
        a.append(l[i] * l[len(l) - i - 1])
    print(a)


Result(l)