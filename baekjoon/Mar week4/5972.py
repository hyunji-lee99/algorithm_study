import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
# dummy
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int, sys.stdin.readline().split(' '))
    graph[a].append((b,c))
    graph[b].append((a,c))

# 가중치순으로 정렬
for i in range(1, n+1):
    graph[i].sort(key=lambda x:x[1])


minvalue=1e9
queue=deque()
queue.append((1,0))
visited=[0]*(n+1)

while queue:
    cur, sumofcow =queue.popleft()
    visited[cur]=1
    if cur==n:
        minvalue=min(minvalue, sumofcow)
    for node, cow in graph[cur]:
        if visited[node]==0:
            queue.append((node, sumofcow+cow))

print(minvalue)




