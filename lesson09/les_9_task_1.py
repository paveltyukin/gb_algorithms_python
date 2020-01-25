'''
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(),
sha1() или любой другой из модуля hashlib задача считается не решённой.
'''

import hashlib, collections


def get_hash(user_str):
    '''
        Функция возвращает словарь - OrderedDict:
        ключи - подстроки, значения - хеши этих подстрок
    '''
    
    # Для проверки с подстрокой на отличие
    # друг от друга согласно заданию.
    user_hash = hashlib.sha1(bytes(user_str, 'utf-8')).hexdigest()

    # Результирующий словарь - OrderedDict:
    # ключи - подстроки, значения - хеши этих подстрок
    dict_hash = {}
    collections.OrderedDict(dict_hash)

    # Прохожусь по циклу, чтобы добавить
    # все подстрроки с хешами в словарь dict_hash.
    for i in range(len(user_str)):
        
        # Временная переменная для хранения подстроки
        symbol_check = ''
        
        # Прохожусь по циклу
        for j in user_str[i:]:
            
            # "Генерирую" подстроку путем добавления
            # оставшейся подстроки из начальной строки.
            symbol_check += j
            
            # Хеширую
            symbol_hash = hashlib.sha1(bytes(symbol_check, 'utf-8')).hexdigest()

            # Проверяю согласно условию
            # "в сумму не включаем пустую строку и строку целиком"
            if symbol_hash != user_hash and symbol_hash not in dict_hash:
                dict_hash[symbol_check] = symbol_hash

    # Возвращяю результат
    return dict_hash

# Проверка и вывод результата
user_str = input('Введите строку: ')
if not user_str:
    print('Повторите ввод!')

user_hash = get_hash(user_str)
print(f'\nСтрока "{user_str}" содержит: {len(user_hash)} хешированных подстрок:\n')

for key, value in user_hash.items():
    print('\t', f'{key} \t- {value}')