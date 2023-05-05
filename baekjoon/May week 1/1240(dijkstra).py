# 가중치가 있는 최단 거리 구하기 -> 다익스트라 알고리즘
import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))

# dummy
graph=[[] for _ in range(n+1)]

# (node, dist) 순으로 저장
for i in range(n-1):
    n1,n2,dist=map(int, sys.stdin.readline().split(' '))
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))

# 거리를 알고 싶은 두 노드 리스트
ans_list=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(m)]

def dijkstra(node1, node2):
    global graph
    # node1에서 node2까지 가는 최단 경로 구하기
    distance=[1e9]*(n+1)
    distance[node1]=0
    queue=deque()
    queue.append(node1)
    visited=[0]*(n+1)
    while queue:
        cur=queue.popleft()
        visited[cur]=1
        for node,dist in graph[cur]:
            if visited[node]==0:
                if distance[cur] + dist < distance[node]:
                    distance[node] = distance[cur] + dist
                queue.append(node)
    return distance[node2]


for node1, node2 in ans_list:
    print(dijkstra(node1, node2))