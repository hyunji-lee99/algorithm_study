#f : 건물의 총 층수
#s : 강호의 현재 위치 층
#g : 스타트링크가 있는 층
#u : 위로 u층만큼 갈 수 있음
#d : 아래로 d층만큼 갈 수 있음
#강호가 스타트링크가 있는 층에 도착하려면 적어도 버튼을 몇 번 눌러야 하는가?

import sys
from collections import deque

f,s,g,u,d=list(map(int, sys.stdin.readline().split(' ')))
#bfs

#init
count=0
queue=deque()
queue.append((s,count))
visited=[0]*(f+1)
#visited를 이런 형식으로 받으면 됨

while queue:
    cur,cur_count=queue.popleft()
    if cur==g:
        print(cur_count)
        sys.exit(0)
    for i in (cur+u,cur-d):
        if 0<i<=f and visited[i]==0:
            visited[i]=1
            queue.append((i,cur_count+1))

print('use the stairs')
sys.exit(0)