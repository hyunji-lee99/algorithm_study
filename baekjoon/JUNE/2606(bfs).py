# 1번 컴퓨터와 연결된 컴퓨터의 수를 구하라

import sys
from collections import deque

n=int(sys.stdin.readline())
pair=int(sys.stdin.readline())
# dummy
network=[[] for _ in range(n+1)]
for _ in range(pair):
    c1,c2=map(int, sys.stdin.readline().split(' '))
    network[c1].append(c2)
    network[c2].append(c1)

visited=[0]*(n+1)
visited[1]=1
queue=deque()
queue.append(1)

ans=0
while queue:
    cur=queue.popleft()
    ans+=1
    for node in network[cur]:
        if visited[node]==0:
            queue.append(node)
            visited[node]=1

# 1번 컴퓨터 제외
ans-=1
print(ans)




