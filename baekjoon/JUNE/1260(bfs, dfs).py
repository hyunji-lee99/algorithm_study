import sys
from collections import deque

n,m,v=map(int, sys.stdin.readline().split(' '))
# 1~n번 노드에 연결된 노드 정보
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int, sys.stdin.readline().split(' '))
    graph[s].append(e)
    graph[e].append(s)

# 그래프 정렬
for g in graph:
    g.sort()

# bfs
def bfs():
    global graph,v
    sequence=[]
    queue=deque()
    queue.append(v)
    visited=[0]*(n+1)
    visited[v]=1
    while queue:
        cur=queue.popleft()
        sequence.append(cur)
        for node in graph[cur]:
            if visited[node]==0:
                queue.append(node)
                visited[node]=1

    return sequence

dfs_visited=[0]*(n+1)
dfs_sequence=[]
def dfs(v):
    global graph, dfs_visited, dfs_sequence
    dfs_sequence.append(v)
    dfs_visited[v]=1
    for node in graph[v]:
        if dfs_visited[node]==0:
            dfs(node)

dfs(v)
print(*dfs_sequence, sep=' ')
print(*bfs(), sep=' ')
