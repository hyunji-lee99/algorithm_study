import sys
from collections import deque
# n : 노드의 개수
# m : 거리를 알고 싶은 노드 쌍의 개수

n,m=map(int, sys.stdin.readline().strip().split(' '))
graph=[[] for _ in range(n+1)]
answer=[]

for i in range(n-1):
    n1,n2,d=map(int, sys.stdin.readline().strip().split(' '))
    graph[n1].append((n2,d))
    graph[n2].append((n1,d))

for i in range(m):
    n1,n2=map(int, sys.stdin.readline().split(' '))
    answer.append((n1,n2))

#bfs
for n1,n2 in answer:
    distance=0
    queue = deque()
    queue.append((n1, 0))
    visited = [0] * (n + 1)
    while queue:
        cur,d=queue.popleft()
        visited[cur]=1
        distance+=d
        if cur==n2:
            break
        for n,d in graph[cur]:
            if visited[n]==0:
                queue.append((n,d))
    print(distance)

#백준에서 index error 발생