'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random

# Создаю рабочий список
work_list = [random.randint(1, 100) for _ in range(10)]

# Создаю список
# из уникальных значений
unique_list = set(work_list)

# Создаю рабочий словарь
work_dict = {}

# Первым проходом создаю
# уникальные элементы в словаре work_dict
for key, value in enumerate(unique_list):
    work_dict[value] = 0

# Ввожу переменные max_n - для номера, 
# max_num - для значения согласно условию задачи
max_n = 0
max_num = 0

# Вторым проходом собираю все значения
# в словаре work_dict
for key, value in enumerate(work_list):

    # Прибавляю по одному, если значения совпадают
    work_dict[value] += 1

    # Сразу же отбираю максимальное значение
    if work_dict[value] > max_n:
        max_n = work_dict[value]
        max_num = value

# Вывожу исходный список
print(work_list)

# Если значения уникальные, то max_n == 1
if max_n == 1:
    print("Все значения уникальные")
# Иначе вывожучисло повторений и само число,
# согласно условию
else:
    print(f'Число повторений - {max_n} у эелемента {max_num}')


# Вариант 2

work_list = [random.randint(1, 100) for _ in range(10)]
print(work_list, 'Вариант 2')
num = work_list[0]

max_num = 1
for i in range(len(work_list)):
    meet = 1
    for k in range(i+1, len(work_list)):
        if work_list[i] == work_list[k]:
            meet += 1
    if meet > max_num:
        max_num = meet
        num = work_list[i]
 
if max_num > 1:
    print(max_num, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')