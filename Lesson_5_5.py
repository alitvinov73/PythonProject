# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f_new = open("lesson_5_5.txt", 'w', encoding='utf-8')
my_sum = 0
print('Function of summary numeric.')

while True:
    num = input("Enter numeric or '*' for end: ")
    if num == '*':
        break
    try:
        num = int(num)
        f_new.write(f'{num} ')
        my_sum += num  # подсчет суммы при вводе данных
    except ValueError:
        print('Please enter only numeric!')
f_new.close()
f_new = open("lesson_5_5.txt", 'r', encoding='utf-8').read()
print(f'You enter values: {f_new}')
print(f'First way: sum this values in cycle with enter data: {my_sum}')

# Two way of summary
print(f'Second way: sum of one string code from read file: '
      f'{sum(list(map(int, open("lesson_5_5.txt", "r", encoding="utf-8").read().split())))}')
