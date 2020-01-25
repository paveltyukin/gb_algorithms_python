'''
1. На улице встретились N друзей.
Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?

Примечание. Решите задачу при помощи построения графа.
'''
# Количество друзей
N = 3

graph_n = [[1 if j > i else 0 for j in range(N)] for i in range(N)]

sum_graph = 0
for row in graph_n:
    sum_graph += sum(row)

print(sum_graph)