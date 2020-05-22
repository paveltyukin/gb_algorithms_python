'''
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''

# Ввожу результирующие переменные
max_sum = max_num = 0

# Запускаю бесконечный цикл
while True:

    # Запрашиваю у пользователя натуральное число
    user_num = int(input('Введите натуральное число или 0 (ноль) для выхода:\n'))

    # Если пользователь ввел 0, то выхожу из цикла
    if not user_num:
        break

    
    # Ввожу текущие переменные 
    # для временного хранения
    cur_num = user_num
    cur_sum = 0

    
    # Прохожусь циклом по user_num
    while cur_num > 0:

        # Последовательно складываю 
        # все цифры в числе, уменьшая cur_num
        cur_sum += cur_num % 10
        cur_num //= 10

    # Если текущее значение суммы больше 
    # максимально полученной до этого момента, 
    # то приравниваю max_sum = cur_sum, аналогично для числа
    if cur_sum > max_sum:
        max_sum = cur_sum
        max_num = user_num

# Вывожу результат
print(max_sum, max_num)