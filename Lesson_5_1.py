# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_data = ' '
f_new = open('new.txt', 'w', encoding='utf-8')

while True:
    my_data = input('Enter data: ')
    if not my_data == '':
        f_new.write(f'{my_data}\n')
        print(f' You data  \'{my_data}\' append in file new.txt:')
    else:
        print('Data entry finished, you data:\n')
        f_new.close()
        f_new = open("new.txt", 'r', encoding='utf-8').read()
        print(f_new)
        break
