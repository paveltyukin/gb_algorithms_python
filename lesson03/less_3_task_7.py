'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
'''

import random

# Устанавливаю 15 элементов в списке
N = 10

# Определяю рабочий список
work_list = [random.randint(0, 100) for _ in range(N)]

# Вывожу на экран исходный список
# и определяю индекс минимального элемента 
print(work_list)
min_n = 0

# Прохожусь по циклу для определения минимального элемента
for idx, value in enumerate(work_list):

    # Если элемент по итерации меньше, чем с индексом min_n,
    # то присваиваю min_n = idx 
    if work_list[idx] < work_list[min_n]:
        min_n = idx

# Определяю первый минимальный элемент в цикле
# в новую переменную и удаляю его 
first_min = work_list[min_n]
del work_list[min_n]

# Аналогично делаю для определения второго минимального элемента
min_n = 0
for i, value in enumerate(work_list):
    if work_list[i] < work_list[min_n]:
        min_n = i

# Вывожу результат
print(f'Первый минимальный элемент списка - {first_min}')
print(f'Первый минимальный элемент списка - {work_list[min_n]}')

# Вариант 2 (Один цикл)

# Определяю исходный список
work_list = [random.randint(0, 100) for _ in range(N)]

# Определяю 2 переменные для исходного списка,
# которые соответствуют 1 и второму элементу.
# Для их использования, необходимо их поставить
# в возрастающий порядок 
if work_list[0] > work_list[1]:
    n1 = 0
    n2 = 1
else:
    n1 = 1
    n2 = 0

# Прохожусь по циклу 1 раз.
# Так как первые 2 элемента уже определены,
# то range() начиналется с 2-ух
for i in range(2, len(work_list)):

    # Если итерационный элемент меньше первого,
    # присваиваю временной переменной значений первого элемента 
    if work_list[i] < work_list[n1]:
        b = n1

        # Присваиваю новое значение переменной n1,
        # так как это значение теперь минимальное.
        n1 = i

        # Остается проверить n1 (b)  по отношению к n2
        if work_list[b] < work_list[n2]:

            # Если условие соблюдается,
            # то присваиваю n2 значение переменной n1 (b)
            n2 = b
    
    # Иначе, если переменная находится больше n1 и меньше n2, 
    # то присваиваю n2 значение переменной i
    elif work_list[i] < work_list[n2]:
        n2 = i

# Выводу результат
print(work_list)
print(work_list[n1], work_list[n2])