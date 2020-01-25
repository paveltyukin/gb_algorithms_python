'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
'''
graph=[
    [0,0,1,1,9,0,0,0],
    [0,0,9,4,0,0,5,0],
    [0,9,0,0,3,0,6,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,5,0],
    [0,0,7,0,8,1,0,0],
    [0,0,0,0,0,1,2,0],
]

def bfs(n,graph,start):
    
    p=preque()
    p.put((0,start,-1))
    used=[-1]*n
    parent=[[]]*n
    
    while not p.empty():
        
        cost,v,rod=p.get()
        if used[v]==-1:
            if v!=start:
                parent[v]=parent[rod] + [rod] + [cost]
            used[v]=cost
            for x in range(n):
                if graph[v][x]>0:
                    p.put((cost+graph[v][x],x,v))
    return used, parent

print(bfs(8,graph,0))