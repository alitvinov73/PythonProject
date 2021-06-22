# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
f_old = open("lesson_5_4.txt", 'r', encoding='utf-8').read().splitlines()
f_new = open("lesson_5_4_new.txt", 'w', encoding='utf-8')
for el in f_old:
     f_new.write(f'{my_dict[el.split()[0]]} - {el.split()[2]}\n')
f_new.close()
f_new = open("lesson_5_4_new.txt", 'r', encoding='utf-8').read()
print(f_new)
