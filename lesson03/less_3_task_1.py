'''
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
'''

# Создаю список длиной 8 из нулей
my_list = [0]*8

# прохожусь по числам огласной условию
for i in range(2, 100):

    # прохожусь по числам согласно условию,
    # в который буду записывать сумму кратных чисел
    for j in range(2, 10):

        # Проверяю на кратность и записываю
        # в список my_list. 
        if i % j == 0:
            my_list[j - 2] += 1

# Вывожу результат
i = 0
while i < len(my_list):
    print(f'{i + 2} - {my_list[i]}')
    i += 1