'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

import random

# Вариант №1

def merge_sort(lst):
    
    if len(lst) <= 1:
        return
    
    middle = len(lst) // 2
    left = [lst[i] for i in range(0,middle)]
    right= [lst[i] for i in range(middle, len(lst))]
    
    merge_sort(left)
    merge_sort(right)
    
    merged = [0]*(len(left) + len(right))
    
    i = k = n = 0

    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            merged[n] = left[i]
            i += 1
            n += 1
        else:
            merged[n] = right[k]
            k += 1
            n += 1
    while i < len(left):
        merged[n] = left[i]
        i += 1
        n += 1
    while k < len(right):
        merged[n] = right[k]
        k += 1
        n += 1

    for i in range(len(lst)):
        lst[i] = merged[i]
    
    return lst
    
lst = [random.randint(0,50) for _ in range(10)]
print(lst)
print(merge_sort(lst))


# Вариант №2

lst = [random.randint(0,50) for _ in range(20)]
print(lst)

def merge_sort_2(lst):
    
    if len(lst) <= 1:
        return lst
    
    middle = int(len(lst)/2)
    
    left = merge_sort_2(lst[:middle])
    right =merge_sort_2(lst[middle:])
    
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if len(left) > 0:
        result += left

    if len(right) > 0:
        result += right
    
    return result

print(merge_sort_2(lst))