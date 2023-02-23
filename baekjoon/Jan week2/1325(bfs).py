#n : 컴퓨터는 n번까지 하나씩 번호가 매겨짐
#m : m줄에 걸쳐서 신뢰관계가 입력됨

import sys
from collections import deque

n,m=map(int, sys.stdin.readline().strip().split(' '))

#신뢰하는 데이터가 아니라 신뢰를 받고 있는 컴퓨터 배열
#예를 들어, trust[i]=[j]이면 j가 i를 신뢰하고 있음
trust=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int, sys.stdin.readline().strip().split(' '))
    trust[b].append(a)

numbers=[]
#bfs
queue=deque()
for idx in range(1, len(trust)):
    number=0
    visited=[0]*(n+1)
    visited[idx]=1
    for node in trust[idx]:
        if visited[node]==0:
            queue.append(node)
            number += 1
            visited[node]=1
    while queue:
        cur=queue.popleft()
        for node in trust[cur]:
            if visited[node]==0:
                queue.append(node)
                number += 1
                visited[node] = 1
    numbers.append(number)

for i in range(len(numbers)):
    if numbers[i]==max(numbers):
        print(i+1,end=' ')






