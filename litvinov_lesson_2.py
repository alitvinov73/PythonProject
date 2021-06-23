# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
a = ['text', 12, 1.5, True]
for el in a:
    print(type(el))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

a = input("Введите список значений, разделенных пробелом: ").split()
print("Введенный список:", a)
i = 1
while i < len(a):
    a[i - 1], a[i] = a[i], a[i - 1]
    i += 2
print("Cписок, где реализован обмен значений соседних элементов:", a)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

n = int(input("Введите номер месяца: "))

# Через list
month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
              "декабрь"]
season_list = ["зима", "весна", "лето", "осень"]
print("Решение через списки: ")
if n == 1 or n == 2 or n == 12:
    print("Месяц " + month_list[n - 1] + " относится к сезону: " + season_list[0])
elif n == 3 or n == 4 or n == 5:
    print("Месяц " + month_list[n - 1] + " относится к сезону: " + season_list[1])
elif n == 6 or n == 7 or n == 8:
    print("Месяц " + month_list[n - 1] + " относится к сезону: " + season_list[2])
else:
    print("Месяц " + month_list[n - 1] + " относится к сезону: " + season_list[3])

# Через dict
month_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябрь", 10: "октябрь", 11: "ноябрь",
              12: "декабрь"}
season_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
print("Решение через словари: ")
if n == 1 or n == 2 or n == 12:
    print("Месяц " + month_dict[n] + " относится к сезону: " + season_dict[1])
elif n == 3 or n == 4 or n == 5:
    print("Месяц " + month_dict[n] + " относится к сезону: " + season_dict[2])
elif n == 6 or n == 7 or n == 8:
    print("Месяц " + month_dict[n] + " относится к сезону: " + season_dict[3])
else:
    print("Месяц " + month_dict[n] + " относится к сезону: " + season_dict[4])


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
s = input("Введите текст: ").split()            # получение текстовой строки, формирование из нее списка по пробелам
i=1                                             # счетчик номера элемента списка
for el in s:
    print(str(i) + ". " + s[i - 1][:10])        # печать номера элемента, срез из 10 первых символов
    i+=1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
spis = [9, 8, 6, 4, 3]
spis.append(int(input("Введите новый элемент рейтинга: ")))            # новый элемент в конце списка
spis.sort(reverse = True)                                              # Обратная сортировка
print(spis)


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно
# сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],  “цена”: [20000, 6000, 2000],  “количество”: [5, 2, 7],  “ед”: [“

n = 1
l_spisok = []

while True:
    ch = True
    print("Введите данные о товаре: ")
    l_spisok.append((n, dict(Наименование=str(input("Наименование: ")),
                             Цвет=str(input("Цвет: ")),
                             Вес=float(input("Вес: ")),
                             Количество=int(input("Количество: "))
                             )
                     )
                    )
    if input('Товар добавлен. Добавить еще один товар? (1/0): ') == '0':
        break
    n += 1
print(f'Список товаров в виде кортежей:{l_spisok}')

print("Аналитика о товарах в виде словаря: ")
my_dict = dict({})
for prod in l_spisok:
    # print(prod)
    # print(prod[-1])
    for n, value in prod[-1].items():
        if n in my_dict:
            if value not in my_dict.get(n):
                my_dict.get(n).append(value)
        else:
            my_dict.update({n: [value]})

print(f' Аналитика: {my_dict}')