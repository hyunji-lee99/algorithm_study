import sys
from collections import deque

# 정점 개수, 간선 개수
n,m=map(int, sys.stdin.readline().strip().split(' '))
graph=[[] for _ in range(n+1)]
graphR=[[] for _ in range(n+1)]

for _ in range(m):
    start, end=map(int, sys.stdin.readline().strip().split(' '))
    graph[start].append(end)
    graphR[end].append(start)

s,t=map(int, sys.stdin.readline().strip().split(' '))

# s에서 도달할 수 있는 노드(t를 거치지 않음), t에서 도달할 수 있는 노드(s를 거치지 않음) 중 공통 노드를 찾는다

# s에서 도달할 수 있는 노드(출근길에 들릴 수 있는 노드)
visited_s=[0]*(n+1)
visited_s[s]=1
queue_s=deque()
queue_s.append(s)
while queue_s:
    cur=queue_s.popleft()
    for node in graph[cur]:
        if visited_s[node]==0 and node!=t:
            queue_s.append(node)
            visited_s[node]=1

# t에서 도달할 수 있는 노드(퇴근길에 들릴 수 있는 노드) 중에 출근길에 들릴 수 있는 노드 찾기
visited_t=[0]*(n+1)
visited_t[t]=1
queue_t=deque()
queue_t.append(t)
while queue_t:
    cur=queue_t.popleft()
    for node in graph[cur]:
        if visited_t[node]==0 and node!=s:
            queue_t.append(node)
            visited_t[node]=1

# s에서 출발해서 도달 가능한 노드들이 t까지 도달할 수 있는지 확인
visited_s_t=[0]*(n+1)
visited_s_t[t]=1
queue_s_t=deque()
queue_s_t.append(t)
while queue_s_t:
    cur=queue_s_t.popleft()
    for node in graphR[cur]:
        if visited_s_t[node]==0:
            queue_s_t.append(node)
            visited_s_t[node]=1

# t에서 출발해서 도달 가능한 노드들이 s까지 도달할 수 있는지 확인
visited_t_s=[0]*(n+1)
visited_t_s[s]=1
queue_t_s=deque()
queue_t_s.append(s)
while queue_t_s:
    cur=queue_t_s.popleft()
    for node in graphR[cur]:
        if visited_t_s[node]==0:
            queue_t_s.append(node)
            visited_t_s[node]=1

ans=0
for i in range(1,n+1):
    if visited_s[i] and visited_t[i] and visited_s_t[i] and visited_t_s[i]:
        ans+=1

print(ans)