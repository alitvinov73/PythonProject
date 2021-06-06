# 5. Реализовать формирование списка, используя функцию range() и
# возможности генератора. В список должны войти четные числа от 100 до 1000
# (включая границы). Необходимо получить результат вычисления произведения
# всех элементов списка.

data = [i for i in range(100, 1000, 2)]

# Вариант 1
res = lambda data: data[0] * res(data[1:]) if data else 1
print(res(data))

# Вариант 2
res = 1
for i in data:
    res *= i
print(res)

# Вариант 3
from functools import reduce
print(reduce(lambda x, y: x * y, data))
