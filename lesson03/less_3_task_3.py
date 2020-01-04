'''
3. В массиве случайных целых чисел
поменять местами минимальный и максимальный элементы.
'''

import random

# Вариант 1

# Генерирую список из 10 элементов
work_list = [random.randint(0, 100) for _ in range(10)]

# Определяю минимальное и максимальное значение,
# как первый элемент списка - порядковый номер элемента,
# а второй элемент списка = первому элементу списка work_list  
min_number = [0, work_list[0]]
max_number = [0, work_list[0]]

# Прохожусь по списку work_list
for key, value in enumerate(work_list):

    # Если знчание списка work_list больше
    # значения первого элемента списка max_number,
    # то это число и нужно, поэтому заменяю его
    #  в списке max_number
    if value > max_number[1]:
        max_number[1] = value
        max_number[0] = key

    # Аналогично для списка min_number
    if value < min_number[1]:
        min_number[1] = value
        min_number[0] = key

# Вывожу на экран исходный список
print(work_list)

# Меняю в списке work_list минимальное
# и максимальное знасчение согласно условию задачи
work_list[max_number[0]], work_list[min_number[0]] = work_list[min_number[0]], work_list[max_number[0]]

# Вывожу на экран окончательный список work_list
print(work_list)


# Вариант 2 (Через вспомагательную переменную и через номера в списке)
work_list = [random.randint(0, 100) for _ in range(20)]

# Создаю номера в списке, 
# значения которых будут максимум и минимум в списке work_list
min_n = 0
max_n = 0

# Прохожусь по списку 
for i in range(len(work_list)):

    # Аналогично предыдущему варианту.
    # Только заменяю номер в переменных, 
    # как min_n, так и max_n
    if work_list[i] < work_list[min_n]:
        min_n = i
    elif work_list[i] > work_list[max_n]:
        max_n = i

# Вывожу список work_list перед заменой
print(work_list)

# Меняю элементы с помощью
# вспомагательной переменной spam
spam = work_list[min_n]
work_list[min_n] = work_list[max_n]
work_list[max_n] = spam

# Вывожу результирующий список
print(work_list)