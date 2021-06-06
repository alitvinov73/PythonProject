# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def salary(hour, pay_in_hour, bonus):
    try:
        return (hour * pay_in_hour)*(1+bonus/100)
    except TypeError:
        print("Input uncorrect value type. You must enter numeric values.")
    return


print("Function of calculate salary of employee. For ended of calculate enter '*' in any name field")

while True:
    name = input('Name of employee: ')
    if name == "*":
        break
    hour = float(input('Input duration of operation in hours: '))
    pay_in_hour = int(input('Input rate in hours: '))
    bonus = int(input('Input bonus in procent of rate in hours: '))
    print(f"Name: {name}, salary is: {round(salary(hour, pay_in_hour, bonus))}")
    print("-"*50)
