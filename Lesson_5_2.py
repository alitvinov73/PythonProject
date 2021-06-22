# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_line = open("lesson_5_2.txt", 'r', encoding='utf-8').readlines()
count_line = []
print(f'Data: {my_line}')
i = 0
for el in my_line:
    count_line.append([i + 1, len(my_line[i].split())]);
    i += 1
print(f' Result: count of lines is: {i}, \n Count of word in lines (number line, words): {count_line}')
