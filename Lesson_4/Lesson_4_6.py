# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет прекращено.

import itertools as it

# а) итератор, генерирующий целые числа, начиная с указанного,
print("Generate integers.")
m_list = []
# Option 1

my_iter = it.count(int(input("Enter start integer: ")), 1)
last_interger = int(input("Enter last interger: "))
for i in my_iter:
    if last_interger >= i:
        m_list.append(i)
    else:
        break
print(m_list)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
data = [2, 7, 23, 44]
print(len(data))
my_data_cycle = it.cycle(data)

while input("Print iterate list (y - 'yes', any other - 'no')?") == "y":
    count = 1
    for i in my_data_cycle:
        print(i)
        if count >= len(data):
            break
        else:
            count += 1
