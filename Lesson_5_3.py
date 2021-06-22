# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# Enter of data
f_new = open("lesson_5_3.txt", 'w', encoding='utf-8')
print('Calculate average salary of staff. If you finished, please enter empty value in name. \n')
while True:
    name = input("Enter name of employee: ")
    if not name == '':
        while True:
            try:
                salary = int(input("Enter salary of employee: "))
                break
            except ValueError:
                print('Please enter only numeric!')
        f_new.write(f'{name}#{str(salary)}\n')
    else:
        print('Data entry finished, you data:\n')
        f_new.close()
        break
# Data Processing
my_staff = open("lesson_5_3.txt", 'r', encoding='utf-8')
average_Salary = 0
i = 0
f_line = my_staff.read().splitlines()

for el in f_line:
    tmp_list = f_line[i].split('#')
    if int(tmp_list[1]) < 20000:
        print(f'The employee \'{tmp_list[0].upper()}\' has a salary of less than 20 000: {tmp_list[1]}')
    average_Salary += int(tmp_list[1])
    i += 1

my_staff.close()
print(f'Average salary of staff: {average_Salary / i}')
