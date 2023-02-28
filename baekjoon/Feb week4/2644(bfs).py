# n : 전체 사람 수
# p1, p2 : 촌수를 계산해야 하는 서로 다른 사람 둘
# m : 부모 자식간의 관계의 개수
# 부모 자식간의 관계를 나타내는 두 번호 입력됨

# 그냥 양방향 그래프에서 특정 노드에서 특정 노드까지 가는 거리를 구하는 문제

import sys
from collections import deque

n=int(sys.stdin.readline())
p1,p2=map(int, sys.stdin.readline().split(' '))
m=int(sys.stdin.readline())

parent=[0]*(n+1)
graph=[[] for _ in range(n+1)]

for i in range(m):
    p,c=map(int, sys.stdin.readline().split(' '))
    graph[p].append(c)
    graph[c].append(p)

queue=deque()
queue.append((p1, 0))
visited=[0]*(n+1)
visited[p1]=1

while queue:
    cur,distance=queue.popleft()
    if cur==p2:
        print(distance)
        sys.exit(0)
    for node in graph[cur]:
        if visited[node]==0:
            queue.append((node, distance+1))
            visited[node]=1

print(-1)


