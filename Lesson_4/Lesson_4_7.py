# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# Factorial Option 1
def fact(n):
    m_fact = 1
    for i in range(1, n + 1):
        m_fact *= i
        yield m_fact

n = int(input("Enter integer for factorial: "))
for el in fact(n):
    print(el)

# Factorial Option 2
# my_factorial = lambda n: n * my_factorial(n - 1) if not n == 1 else 1
# print(my_factorial(n))
