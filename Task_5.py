# Задача № 5
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [-2, -1]:
        return -1
    elif n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return fib(n+1) + fib(n+2)
    else:
        return fib(n-1) + fib(n-2)


a = int(input())
lst = []

for i in range(-a, 1):
    lst.append(fib(i))


for j in range(1, a + 1):
    lst.append(fib(j))
print(lst)
