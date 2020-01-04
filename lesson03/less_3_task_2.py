'''
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5 
(помните, что индексация начинается с нуля), 
т. к. именно в этих позициях первого массива стоят четные числа.
'''
import random

# Генерирую случайный список из 10 элементов
user_list = [random.randint(0,9) for _ in range(10)]

# Создаю результирующий список
result_list = result_list2 = []


# Вариант 1 (в одну строку)

# в одну строку записываю решение через list comprehensions
result_list = [key for key, value in enumerate(user_list) if not value % 2]

# Вариант 2 (много строк)

# Аналогично предыдущему варианту,
# только развертываю все на несколько строк 
for key, value in enumerate(user_list):
    if not value % 2:
        result_list2.append(key)

# Вывожу результат
print(f'{user_list} - Исходный список')
print(result_list)
print(result_list2)

