# 위상정렬(Topological Sorting) -> 사이클이 없는 단방향 그래프에서만 사용가능(DAG)
# 순서가 정해져있는 작업을 차례로 수행해야 할 때, 그 순서를 결정해주기 위해 사용하는 알고리즘
# 1. 진입차수가 0인 노드를 큐에 삽입
# 2. 큐에서 원소를 꺼내서 해당 원소와 연결된 간선을 모두 제거
# 3. 제거한 후에 진입차수가 0인 노드를 큐에 삽입
# 4. 2~3번 반복하다, 큐가 비워지면 종료

import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
graph=[[] for _ in range(n+1)]
# 진입차수 저장 배열
inputnumber=[0]*(n+1)

for _ in range(m):
    a,b=map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    inputnumber[b]+=1

line=[]
queue=deque()
# 진입차수 0인 노드 queue에 추가
for i in range(1,n+1):
    if inputnumber[i]==0:
        queue.append(i)

while queue:
    cur=queue.popleft()
    line.append(cur)
    while graph[cur]:
        node=graph[cur].pop(0)
        inputnumber[node]-=1
        if inputnumber[node]==0:
            queue.append(node)

for node in line:
    print(node, end=' ')







