'''
3. Написать программу, 
которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).

Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

from random import randint as rand

def bfs(n,graph,start):
    g=[start]
    used=[-1]*n
    used[start]=0
    while len(g)>0:
        h=[]
        for x in g:
            for y in range(n):
                if graph[x][y] and used[y]==-1:
                    h.append(y)
                    used[y]=used[x]+1
        g=h
    return used

def generate(n):
    i=[[rand(0,1) for y in range(n)] for x in range(n)]
    for x in range(n):
        i[x][x]=0
    return i

# Проверка 
h=generate(5)
for x in range(5):
    print(h[x])
print()
j=bfs(5,h,0)
for x in range(5):
    print(j[x])
print()