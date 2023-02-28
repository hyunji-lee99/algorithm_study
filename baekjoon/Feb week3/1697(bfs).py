# 수빈이와 동생의 위치가 주어질 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하라
# n : 현재 수빈이의 위치
# k : 현재 동생의 위치

import sys
from collections import deque

n,k=map(int, sys.stdin.readline().strip().split(' '))

#bfs
# queue, visited, min init
queue=deque()
queue.append((n,0))
visited=[0]*100002
min=1e9

while queue:
    cur,time=queue.popleft()
    visited[cur]=1
    if cur==k:
        if min>time:
            min=time
            break
    for next in (cur+1,cur-1,cur*2):
        #범위 설정에서 next가 0보다 커야 한다는 걸 빼먹어서 인덱스에러 계속 발생
        #처음에 visited=[]로 두고, 추가해주면서 not in으로 방문여부를 탐색해줘서 시간초과 발생
        if 0<=next<=100000 and visited[next]==0:
            queue.append((next,time+1))

print(min)