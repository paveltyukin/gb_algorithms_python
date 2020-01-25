'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''

from collections import Counter, defaultdict
from heapq import heappush, heappop, heapify
from bitarray import bitarray

# класс Node:
# для ветвей дерева - внутренних узлов;
class Node: 
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def walk(self, code, acc):
        """
            Для обхода правого потомка добавляется "1", а девого "0".
        """
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

# Класс для листьев дерева,
# у него нет потомков, но есть значение символа
class Leaf:
    
    def __init__(self, char):
        self.char = char
    
    def walk(self, code, acc):
        """
            Функция устанавливает либо "0" либо acc, если acc не равен ""
        """
        code[self.char] = acc or "0"

def huffman_encode(s):
    """
        Функция возвращает словарь кодирования строки в коды Хаффмана
    """

    # Ввожу очередь с приоритетами
    h = []
    
    # Добавляю счетчик Counter() для символов из введеднной пользователем строки
    # Прохожусь по циклу
    for ch, freq in Counter(s).items():
        
        # Очередь состоит из частоты символа, счетчика и самого символа
        h.append((freq, len(h), Leaf(ch)))

    # Строю очередь с приоритетами
    heapify(h)
    
    # Инициализирую значение счетчика длиной очереди
    count = len(h)
    
    # Пока в очереди есть хотя бы 2 элемента
    while len(h) > 1:
        
        # Вытаскиваю последовательно элементы с минимальной частотой - левый и правый узлы
        freq1, _count1, left = heappop(h)
        freq2, _count2, right = heappop(h)
        
        # Добавляю в очередь новый элемент,
        # у которого частота равна суме частот, вытащенных элементов.
        # Добавляю новый узел Node(left, right)
        heappush(h, (freq1 + freq2, count, Node(left, right)))
        
        count += 1

    # Ввожу результирующую переменную code (коды символов)
    code = {}
    
    # Если строка пустая, то очередь будет пустая и обходить нечего
    if h:
        
        # В очереди 1 элемент, приоритет которого не важен,
        # а сам элемент - корень дерева
        [(_freq, _count, root)] = h
        
        # обойдем дерево от корня
        # и заполним словарь для получения кодирования Хаффмана
        root.walk(code, "")

    # Возвращаю словарь символов и соответствующих им кодов
    return code


# Введите строку
s = input('Введите строку:\n')

# Кодирую строку с huffman_encode()
code = huffman_encode(s)

# Каждое значение из code конкатенирую в результат encoded
encoded = "".join(code[ch] for ch in s)

# Вывожу результат
print(f'Число символов: {len(code)}')
print(f'Длина закодированной строки: {len(encoded)}')

# Прохожусь по отсортированному словарю code
# и вывожу символ и соответствующий ему код
for ch in sorted(code):
    print(f'{ch} \t- {code[ch]}')

# Вывожу закодированную строку
print(encoded)

# Вариант 2

user_text = input('Введите строку:\n')

# Создаю defaultdict и добавляю в него
# уникальные символы из user_text
freq_lib = defaultdict(int)
for ch in user_text:
    freq_lib[ch] += 1

# Преобразую к списку
heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]
heapify(heap)

while len(heap) > 1:
    
    # heappop - возвращает наименьшее значение из heap
    right = heappop(heap)
    left = heappop(heap)

    # Добавляю "0" к right
    for pair in right[1:]:
        pair[1] = '0' + pair[1]
    
    # Добавляю "1" к left
    for pair in left[1:]:
        pair[1] = '1' + pair[1]
    
    # Добавляю значения в heap
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])


huffman_list = right[1:] + left[1:]
for ch in huffman_list:
    print(f'{ch[0]} \t- {ch[1]}')

huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}
print(huffman_dict)

encoded_text = bitarray()
encoded_text.encode(huffman_dict, user_text)

print(encoded_text)