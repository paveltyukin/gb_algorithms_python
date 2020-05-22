'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — цифры числа.

Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Примечание:
Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, 
задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления
в другую в данной задаче под запретом.

Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
'''
import collections
# Использование см. строку: 169

# Вариант №1

# Запрашиваю у польщователя числа,
# делаю из них список
num_1, num_2 = list(input('ВВедите:\n')), list(input('ВВедите:\n'))


def delete_zero(check_list):
    
    # Убираю первые нули
    check_str = ''.join(check_list)
    first_symbol = check_str[0]

    while first_symbol == '0':
        check_str = check_str[1:]
        first_symbol = check_str[0]

    return check_str


def sum_16_1(num_1, num_2):

    # Переворячиваю числа
    num_1, num_2 = num_1[::-1], num_2[::-1]
    num_sum = []
    num_list = '0123456789ABCDEF'

    # Если длины неодинаковые, то добавляю "0" в список, какой меньше в конец
    # Мне так удобней

    if len(num_1) != len(num_2):
        if len(num_1) > len(num_2):
            for i in range(len(num_1) - len(num_2)):
                num_2.append("0")
        else:
            for i in range(len(num_2) - len(num_1)):
                num_1.append("0")

    # "на ум пошло" - при сложении в столбик
    go_mind = 0

    # Прохожусь по циклу для сложения
    # в 16-ой системе счисления
    for i in range(len(num_1)):

        # Беру числа из 16 СС и складываю
        # их вместе с предыдущим go_mind
        num1 = num_list.index(str(num_1[i]))
        num2 = num_list.index(str(num_2[i]))
        numsum = num1 + num2 + go_mind

        # Вычисляю текущий go_mind и numsum
        go_mind = numsum // 16
        numsum = numsum % 16

        # Добавляю в num_sum из списка num_list
        num_sum.append(num_list[numsum])

    # Добавляю в конец, если есть go_mind
    if go_mind:
        num_sum.append(go_mind)

    # Возвращаю reverse список
    return num_sum[::-1]

# Можно было в одну строку, но мне так удобней
print('Вариант №1. Сумма:')
sum_with_zero = sum_16_1(num_1, num_2)
print(delete_zero(sum_with_zero))

def milti_16_1(num_1, num_2):
    num_1, num_2 = num_1[::-1], num_2[::-1]
    num_list = '0123456789ABCDEF'

    # Аналогично сумме добавляю "0" в конец
    if len(num_1) != len(num_2):
        if len(num_1) > len(num_2):
            for i in range(len(num_1) - len(num_2)):
                num_2.append("0")
        else:
            for i in range(len(num_2) - len(num_1)):
                num_1.append("0")

    # Ввожу необходимые переменные
    num_len = 0
    prev_multi = []
    line_multi = []

    # Аналогично сумме прохожусь по списку и считаю произведение каждого символа
    # одного числа на другое число, то есть умножение в столбик.
    # В принципе, вычисления аналогично сумме
    for key, _ in enumerate(num_1):
        spam_des = 0
        num_len = 0

        while num_len < len(num_2):

            num1 = num_list.index(num_1[key])
            num2 = num_list.index(num_2[num_len])

            spam_multi = num1 * num2 + spam_des

            spam_des = spam_multi // 16
            spam_multi %= 16

            line_multi.append(num_list[spam_multi])

            num_len += 1

        if spam_des:
            line_multi.append(spam_des)

        if key > 0:
            for i in range(key):
                line_multi.insert(0, '0')

        prev_multi.append(line_multi[::-1])
        line_multi = []
        spam_des = 0

    # Если числа умножаются больше чем однозначные,
    # то вычисляю сумму данных чисел используя сумму
    prev_multi_sum = prev_multi[0]
    if len(prev_multi) > 1:
        for i in range(1, len(prev_multi)):
            prev_multi_sum = sum_16_1(prev_multi_sum, prev_multi[i])

    return prev_multi_sum

# Аналогично сумме
print('Вариант №1. Произведение:')
multi_with_zero = milti_16_1(num_1, num_2)
print(delete_zero(multi_with_zero))

# Вариант №2. Перевожу в 10-ую систему счисления, там считаю, перевожу в 16-ую обратно
# Согласно условия задачи:
# "... использование встроенных функций для перевода из одной системы счисления в другую
# в данной задаче под запретом."
# Я использую свою функцию для перевода из 16 в 10 СС

def dec_to_hex(num):
    """
        Функция переводит из 10-ой системы счиления
        в 16-ую систему счисления символы
    """
    # Согласно условию задания 
    # необходимо использовать модуль collections
    hex_list = list('0123456789ABCDEF')
    deque_hex = collections.deque(hex_list)

    spam_hex = ''

    if not num:
        return '0'

    while True:
        spam_hex = f'{spam_hex}{deque_hex[num % 16]}'
        num //= 16

        if not num:
            break

    return ''.join(list(spam_hex)[::-1])

def hex_to_dec(num):
    """
        Функция переводит из 16-ой системы счиления
        в 10-ую систему счисления символы
    """
    hex_str = '0123456789ABCDEF'
    num_list = list(str(num))
    spam_dec = 0

    for key, value in enumerate(num_list):
        spam_dec += hex_str.index(value)*pow(16, len(num_list) - 1 - key)

    return spam_dec


sum_dec = hex_to_dec(''.join(num_1)) + hex_to_dec(''.join(num_2))
multi_dec = hex_to_dec(''.join(num_1)) * hex_to_dec(''.join(num_2))

print('Вариант №2. Сумма:')
print(dec_to_hex(sum_dec))
print('Вариант №2. Произведение:')
print(dec_to_hex(multi_dec))
