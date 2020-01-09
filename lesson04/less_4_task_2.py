'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. 
Функция нахождения простого числа должна принимать на вход натуральное 
и возвращать соответствующее простое число. 

Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».

Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. 
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.

Пример работы программ:
    sieve(2)
3
    prime(4)
7
    sieve(5)
11
    prime(1)
2
'''

import cProfile

# Вариант №1. Решето Эратосфена (см. Урок 2, часть 5)
def sieve_eratosthenes(index):
    idx = index * 500
    sieve = [i for i in range(idx)]

    sieve[1] = 0

    for i in range(2, idx):
        if sieve[i] != 0:
            j = i * 2
            while j < idx:
                sieve[j] = 0
                j += i

    sieve_simple_num = [i for i in sieve if i != 0]
    return sieve_simple_num[index-1]

# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.sieve_eratosthenes(1)"
# 1000 loops, best of 5: 197 usec per loop
# cProfile.run('sieve_eratosthenes(1)')
# 6 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_2.py:29(sieve_eratosthenes)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.sieve_eratosthenes(10)"
# 1000 loops, best of 5: 2.38 msec per loop
# cProfile.run('sieve_eratosthenes(10)')
# 6 function calls in 0.002 seconds
# 1    0.002    0.002    0.002    0.002 less_4_task_2.py:29(sieve_eratosthenes)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.sieve_eratosthenes(100)"
# 1000 loops, best of 5: 27.5 msec per loop
# cProfile.run('sieve_eratosthenes(100)')
# 6 function calls in 0.027 seconds
# 1    0.020    0.020    0.027    0.027 less_4_task_2.py:29(sieve_eratosthenes)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.sieve_eratosthenes(1000)"
# 1000 loops, best of 5: 395 msec per loop
# cProfile.run('sieve_eratosthenes(1000)')
# 6 function calls in 0.635 seconds
# 1    0.500    0.500    0.621    0.621 less_4_task_2.py:29(sieve_eratosthenes)

# Вариант №2. Длинный со списками.

def prime_1(index):
    num = 3
    simple_nums = [2]
    nums = [2]
    while True:
        if len(simple_nums) == index:
            return simple_nums[index-1]
        else:
            for i in nums:
                if num % i == 0:
                    nums.append(num)
                    break
            else:
                nums.append(num)
                simple_nums.append(num)
        num += 1


# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_1(1)"
# 1000 loops, best of 5: 390 nsec per loop
# cProfile.run('prime_1(1)')
# 5 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_2.py:71(prime_1)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_1(10)"
# 1000 loops, best of 5: 19.5 usec per loop
# cProfile.run('prime_1(10)')
# 68 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_2.py:71(prime_1)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_1(100)"
# 1000 loops, best of 5: 2.72 msec per loop
# cProfile.run('prime_1(100)')
# 1182 function calls in 0.003 seconds
# 1    0.003    0.003    0.003    0.003 less_4_task_2.py:71(prime_1)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_1(1000)"
# 1000 loops, best of 5: 542 msec per loop
# cProfile.run('prime_1(1000)')
# 16838 function calls in 0.962 seconds
# 1    0.958    0.958    0.961    0.961 less_4_task_2.py:71(prime_1)

# Вариант №3. Короткий.
    
def prime_2(index):

    count = 1
    k = 2
    while count < index:
        k += 1
        for i in range(2, k):
            if k % i == 0:
                break
        else:
            count += 1
    return k

# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_2(1)"
# 1000 loops, best of 5: 411 nsec per loop
# cProfile.run('prime_2(1)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_2.py:115(prime_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_2(10)"
# 1000 loops, best of 5: 50.7 usec per loop
# cProfile.run('prime_2(10)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_2.py:115(prime_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_2(100)"
# 1000 loops, best of 5: 4.54 msec per loop
# cProfile.run('prime_2(100)')
# 4 function calls in 0.005 seconds
# 1    0.005    0.005    0.005    0.005 less_4_task_2.py:115(prime_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_2" "less_4_task_2.prime_2(1000)"
# 1000 loops, best of 5: 405 msec per loop
# cProfile.run('prime_2(1000)')
# 4 function calls in 1.190 seconds
# 1    1.190    1.190    1.190    1.190 less_4_task_2.py:115(prime_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Вывод
# 1. Алгоритм с решетом Эратосфена медленно работает с большими данными, 
# потому что достаточно сложен. Это связано с тем, что чем больше число, тем больше 
# само "решето", поэтому его тяжело обрабатывать.
# При увеличении данных в 10 раз, время работы алгоритма увеличивается также в 10 раз
#
# 2. Без решета Эратосфена реализованы варианты 2 и 3. Вариант 2 быстрее, 
# потому что сохранение идет в список в одну итерацию и дальше идет работа
# с этим списком. Вариант 3 аналогичен варианту 2, но сохранения нет. 
# Эксперимент показывает, что при увеличении введенных данных в 10 раз, 
# время выполнения алгоритма увеличивается больше, чем в 10 раз (от 20 до 200), 
# как у варианта 2, так и у варианта 3.
# 
# До 1000 числа я бы выбрал вариант №2, как самый быстрый, но время показало, 
# что самый быстрый в моем конкретном случае на больших данных является
# алгоритм решето Эратосфена.