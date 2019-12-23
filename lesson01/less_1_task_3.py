'''
3. Написать программу, которая генерирует в указанных пользователем границах:
3.1. случайное целое число,
3.2. случайное вещественное число,
3.3. случайный символ.
'''
from random import random

# 3.1. Случайное целое число.
# Запрашиваю у пользователя 2 целых числа
print("Введите два целых числа:")
int_start = int(input("Первое:\n"))
int_finish = int(input("Второе:\n"))

# Вычисляю длину диапазона.
# Так как округление до целого числа
# без учета чисел после запятой, то прибавляю 1
# Прибавляю минимум (int_start).
# Получаю случайное целое число от int_start до int_finish
int_random = int(random() * (int_finish - int_start + 1)) + int_start
print(f'Случайное целое число между {int_start} и {int_finish}: {int_random}')

# 3.2. Случайное вещественное число. 
# Запрашиваю у пользователя 2 вещественных числа
print("Введите два вещественных числа:")
float_start = float(input("Первое:\n"))
float_finish = float(input("Второе:\n"))

# Вычисляю длину диапазона.
# Умножаю на генератор. Прибавляю минимум.
float_random = random() * (float_finish - float_start) + float_start
print(f'Случайное вещественное число между {float_start} и {float_finish}: {round(float_random, 2)}')

# 3.3. Случайный символ.
# Запрашиваю у пользователя 2 символа
print("Введите два символа:")
symbol_start = ord(input("Первый:\n"))
symbol_finish = ord(input("Второй:\n"))

# Вычисляю длину диапазона.
# Аналогично первому случаю
symbol_random = int(random()*(symbol_finish - symbol_start + 1)) + symbol_start
print(f'Случайный символ между {chr(symbol_start)} и {chr(symbol_finish)}: {chr(symbol_random)}')
