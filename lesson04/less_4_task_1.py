'''
1. Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:

a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
   (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

------------------------------------------------------------------------

Беру задачу lesson03/less_3_task_3.py
  3. В массиве случайных целых чисел
     поменять местами минимальный и максимальный элементы.
'''


import cProfile
import timeit
import random
import numpy as np
import sys


sys.setrecursionlimit(100000)

def change_min_max_3(N):
    w_list = [random.randint(0, 100) for _ in range(N)]
    
    mn = w_list.index(min(w_list))
    mx = w_list.index(max(w_list))
    
    w_list[mn], w_list[mx] = w_list[mx], w_list[mn]


# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_3(100)"
# 1000 loops, best of 5: 296 usec per loop
# cProfile.run('change_min_max_3(100)')
# 545 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_1.py:31(change_min_max_3)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_3(1000)"
# 1000 loops, best of 5: 2.02 msec per loop
# cProfile.run('change_min_max_3(1000)')
# 5273 function calls in 0.002 seconds
# 1    0.000    0.000    0.002    0.002 less_4_task_1.py:27(change_min_max_3)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_3(10000)"
# 1000 loops, best of 5: 17.2 msec per loop
# cProfile.run('change_min_max_3(10000)')
# 52711 function calls in 0.025 seconds
# 1    0.000    0.000    0.025    0.025 less_4_task_1.py:27(change_min_max_3)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def change_min_max_4(N):
    w_list = [random.randint(0, 100) for _ in range(N)]
    
    def _change_min_max_4(idx, mn, mx):

        if len(w_list) > idx:    
            if w_list[idx] < w_list[mn]:
                mn = idx
            elif w_list[idx] > w_list[mx]:
                mx = idx
                
            return _change_min_max_4(idx+1, mn, mx)

        elif len(w_list) == idx:
            w_list[mx], w_list[mn] = w_list[mn], w_list[mx]
    
    _change_min_max_4(0, 0, 0)


# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_4(100)"
# 1000 loops, best of 5: 231 usec per loop
# cProfile.run('change_min_max_4(100)')
# 733 function calls (633 primitive calls) in 0.000 seconds
# 101/1    0.000    0.000    0.000    0.000 less_4_task_1.py:61(_change_min_max_4)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_4(1000)"
# 1000 loops, best of 5: 3.57 msec per loop
# cProfile.run('change_min_max_4(1000)')
# 7292 function calls (6292 primitive calls) in 0.006 seconds
# 1001/1    0.002    0.000    0.002    0.002 less_4_task_1.py:61(_change_min_max_4)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_4(10000)"
# 1000 loops, best of 5: 27 msec per loop
# cProfile.run('change_min_max_4(10000)')
# 72787 function calls (62787 primitive calls) in 0.078 seconds
# 10001/1    0.024    0.000    0.025    0.025 less_4_task_1.py:61(_change_min_max_4)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def change_min_max_2(N):
    w_list = np.random.randint(0, 100, N)
    
    mn = np.argmin(w_list)
    mx = np.argmax(w_list)
    
    w_list[mn], w_list[mx] = w_list[mx], w_list[mn]



# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_2(100)"
# 1000 loops, best of 5: 7.85 usec per loop
# cProfile.run('change_min_max_2(100)')
# 13 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_1.py:96(change_min_max_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_2(1000)"
# 1000 loops, best of 5: 21.2 usec per loop
# cProfile.run('change_min_max_2(1000)')
# 13 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_1.py:96(change_min_max_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_2(10000)"
# 1000 loops, best of 5: 201 usec per loop
# cProfile.run('change_min_max_2(10000)')
# 13 function calls in 0.002 seconds
# 1    0.000    0.000    0.002    0.002 less_4_task_1.py:96(change_min_max_2)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def change_min_max_1(N):
    work_list = [random.randint(0, 100) for _ in range(N)]

    min_n = 0
    max_n = 0

    for i in range(len(work_list)):
        if work_list[i] < work_list[min_n]:
            min_n = i
        elif work_list[i] > work_list[max_n]:
            max_n = i

    spam = work_list[min_n]
    work_list[min_n] = work_list[max_n]
    work_list[max_n] = spam


# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_1(100)"
# 1000 loops, best of 5: 173 usec per loop
# cProfile.run('change_min_max_1(100)')
# 534 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_1.py:126(change_min_max_1)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_1(1000)"
# 1000 loops, best of 5: 1.92 msec per loop
# cProfile.run('change_min_max_1(1000)')
# 5261 function calls in 0.003 seconds
# 1    0.000    0.000    0.003    0.003 less_4_task_1.py:126(change_min_max_1)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_1(10000)"
# 1000 loops, best of 5: 24.9 msec per loop
# cProfile.run('change_min_max_1(10000)')
# 52711 function calls in 0.085 seconds
# 1    0.016    0.016    0.085    0.085 less_4_task_1.py:126(change_min_max_1)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def change_min_max_5(N):
    work_list = [random.randint(0, 100) for _ in range(N)]

    min_n = 0
    max_n = 0
    i = 0

    while i < len(work_list):
        if work_list[i] < work_list[min_n]:
            min_n = i
        elif work_list[i] > work_list[max_n]:
            max_n = i
        
        i += 1
        
    spam = work_list[min_n]
    work_list[min_n] = work_list[max_n]
    work_list[max_n] = spam


# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_5(100)"
# 1000 loops, best of 5: 214 usec per loop
# cProfile.run('change_min_max_5(100)')
# 640 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 less_4_task_1.py:162(change_min_max_5)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_5(1000)"
# 1000 loops, best of 5: 2.07 msec per loop
# cProfile.run('change_min_max_5(1000)')
# 6285 function calls in 0.005 seconds
# 1    0.000    0.000    0.005    0.005 less_4_task_1.py:162(change_min_max_5)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# python -m timeit -n 1000 -s "import less_4_task_1" "less_4_task_1.change_min_max_5(10000)"
# 1000 loops, best of 5: 28.8 msec per loop
# cProfile.run('change_min_max_5(10000)')
# 62633 function calls in 0.062 seconds
# 1    0.009    0.009    0.062    0.062 less_4_task_1.py:162(change_min_max_5)
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Самый быстрый результат (примерно в 30 раз) получился с использованием 
# библиотеки numpy. 
# Сложность остальных алгоритмов от входных данных линейна (O(n)). При использовании
# while время выполнения алгоритма выше, чем при использовании for. Поэтому for более
# предпочтительней в данной задаче, чем while. С другой стороны при использовании 
# встроенных функций min, max время также чуть меньше, чем при использовании самописного
# поиска min, max через for и while. Рекурсивный алгоритм по времени аналогичен алгориту 
# с использованием while.
# Можно сделать вывод:
#   функция с оптимальным алгоритмом является change_min_max_3