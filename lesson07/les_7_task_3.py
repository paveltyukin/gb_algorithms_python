'''
3. Массив размером 2m + 1, где m — натуральное число, 
заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, используйте метод сортировки, 
который не рассматривался на уроках (сортировка слиянием также недопустима).
'''

import random
import numpy as np

# Определяю медиану списка (номер элемента),
# нахожу минимальный элемент, удаляю его, увеличиваю счетчик на 1
# Вариант 1 (Использование min)

Nmax = 100
N = 5
f = 2*N + 1
lst_1 = [random.randint(1,Nmax) for _ in range(f)]
med_idx = len(lst_1) // 2 + 1

print(lst_1)
def find_minimum(lst, med_idx=0, el_idx=0, first=False):
    el = min(lst)
    lst.remove(el)
    el_idx += 1
    
    if med_idx == el_idx:
        return min(lst)
    
    return find_minimum(lst=lst, med_idx=med_idx, el_idx=el_idx, first=False)

print(find_minimum(lst=lst_1, med_idx=med_idx, el_idx=1, first=True))

# Вариант №2 (Использование цикла для поиска минимума в списке)

lst_2 = [random.randint(1,100) for _ in range(f)]
print(lst_2)


def find_minimum_2(lst, med_idx=0, el_idx=0, first=False):
    mn = 0
    
    for key,value in enumerate(lst):
        if lst[key] < lst[mn]:
            mn = key
    
    
    el = lst[mn]
    lst.remove(el)
    el_idx += 1
    
    if med_idx == el_idx:
        for key,value in enumerate(lst):
            if lst[key] < lst[mn]:
                mn = key
        return lst[mn]
    
    return find_minimum(lst=lst, med_idx=med_idx, el_idx=el_idx, first=False)

print(find_minimum_2(lst=lst_2, med_idx=med_idx, el_idx=1, first=True))

# С помощью сортировок
# Согласно условию задания рассмотрел поразрядную сортировку и пирамидальную
# Вариант №3 (Поразрядная сортировка)
def radix_sort(items, base=10):

    def list_to_buckets(items, base, i):
        buckets = [[] for x in range(base)]
        pBase = base ** i
        for x in items:
            digit = (x // pBase) % base
            buckets[digit].append(x)
        return buckets

    def buckets_to_list(buckets):
        result = []
        for bucket in buckets:
            for number in bucket:
                result.append(number)
        return result

    maxVal = max(items)

    i = 0
    while base ** i <= maxVal:
        array = buckets_to_list(list_to_buckets(items, base, i))
        i += 1

    return array

lst_3 = [random.randint(1,100) for _ in range(f)]
print(lst_3)
sorted_radix = radix_sort(lst_3, base=Nmax)
print(sorted_radix[med_idx-1])


# Вариант №4 (Пирамидальная сортировка)
def heapify(nums, heap_size, root_index):  
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении, 
    # уменьшая счётчик i на 1 
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

lst_4 = [random.randint(1,100) for _ in range(f)]
print(lst_4)
heap_sort(lst_4)
print(lst_4[med_idx-1])