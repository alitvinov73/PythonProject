# Type of data


# Function

# m_f = lambda p_1, p_2: p_1 ** p_2
# print(m_f(2, 8))
# Функция лямбда

# print((lambda p_1, p_2=3: p_1 ** p_2)(2))

# a=['fir1','second2','thrd3']
# a.sort(key=len)
# print(a)
# sorted(a)
# print(a)
# a.sort(key=lambda i: i[-1])
# print(a)


# # Генерация набора ТОЛЬКО ЦЕЛЫХ чисел
# print(list(range(-10, 10, 2)))
# print(range(10))
# print(list(range(10)))
#
# for i in range(len(m_list := [9, 7, 6])):
#     print(m_list[i])
#

# # 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
# # у пользователя, предусмотреть обработку ситуации деления на ноль.
def divided(n_1, n_2):
    """ Функция деления"""
    if n_2 == 0:
        res = "Ошибка деления на 0"
    else:
        res = n_1 / n_2
    return res


def input_num(number=0, m_type=False):
    """Функция ввода чисел
    number - номер числа ввода, если отсутствует то пустая строка
    m_type = тип числа, True - float, False - numeric
    """

    if number == 0:
        number = ""
    while True:
        try:
            if m_type:
                res = float(input(f"Введите число {number}:"))
            else:
                res = int(input(f"Введите число {number}:"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            break
    return res




print("Задание №1. Функция деления чисел: ")
print(f"Результат деления чисел {divided(input_num(1), input_num(2))}:\n")


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.

def person_info(name, surname, birth_year, city, e_mail, phone):
    print(
        f"Name: {name}\nSurname: {surname}\nBirth year: {birth_year}\nCity: {city}\ne-mail: {e_mail}\nPhone number: {phone}")


print("Задание №2. Функция вывода данных о пользователе одной строкой: ")
person_info(name="Ivan", surname="Ivanov", birth_year=2020, city="Moscow", e_mail="ivan_ivanov@mail.ru",
            phone="+7-918-220-52-52")


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.
def my_func(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    my_list.sort(reverse=True)
    return f"{my_list[0]} + {my_list[1]} = {my_list[0] + my_list[1]}"


print("Задание №3. Функция, которая принимает три позиционных аргумента, и возвращает сумму наибольших двух:")
n_1, n_2, n_3 = input_num(1), input_num(2), input_num(3)
print(f"Сумма двух наибольших чисел: {my_func(n_1, n_2, n_3)}")


# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй
# — более сложная реализация без оператора **, предусматривающая использование цикла.

def exponentiation_1(x, y):
    return x ** y


def exponentiation_2(x, y):
    res = 1
    for i in range(0, y):
        res = res * x
    return res


print("Задание №4. Функция возведения в степень:")
print(f"Возведение в степень вариант 1: {exponentiation_1(input_num(1, True), input_num(2))}")
print(f"Возведение в степень вариант 2: {exponentiation_2(input_num(1, True), input_num(2))}")


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def sum_number(isum):
    return sum(isum)


my_sum = 0
print(
    "Задание №5. Введите числа, разделенные пробелом, для прекращения ввода в строку ввода в любом месте введите символ *")
while True:
    print(f"\nТекущая сумма равна: {my_sum}")
    m_str = input("Введите числа, разделенные пробелом: ")
    try:
        if m_str.find("*") == -1:
            m_str = m_str.split()
            m_data = (float(x) for x in m_str)
            my_sum = my_sum + sum_number(m_data)
        else:
            m_str = m_str[:m_str.find("*")].split()
            m_data = (float(x) for x in m_str)
            my_sum = my_sum + sum_number(m_data)
            break
    except ValueError or TypeError:
        print("Error! Это не число, попробуйте снова.")

print(f"Итоговая сумма равна: {my_sum}")


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но
# с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func(my_str):
    res = ""
    for el in my_str.split():
        print(el)
        if not el.isascii() or not el.isalpha() or not el.islower():
            print("Ошибка. Строка должна состоять из маленьких латинских букв.")
            return
        else:
            res += " " + el.title()
    return res


print("\nЗадание №5. Преобразование букв в верхний регистр.")
print(f"Одно слово, первая прописная буква: {int_func(input('Введите слово: '))} ")
print(f"Строка, каждое слово с  прописной буквы: {int_func(input('Введите текст: '))}")
