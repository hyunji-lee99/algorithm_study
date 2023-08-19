import sys
sys.setrecursionlimit(100000)

n,r,q=map(int, sys.stdin.readline().split(' '))
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)
def dfs(v):
    visited[v]+=1
    for node in graph[v]:
        if visited[node]==0:
            visited[v]+=dfs(node)
    return visited[v]

dfs(r)

for _ in range(q):
    root=int(sys.stdin.readline())
    print(visited[root])








