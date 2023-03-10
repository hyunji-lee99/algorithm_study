# 부신 적이 있는 경우와 부신 적이 없는 경우의 visited를 분리해주는 것이 관건이었음!

import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
graph=[]
for i in range(n):
    tmp=list(map(int, sys.stdin.readline().strip()))
    graph.append(tmp)

queue=deque()
queue.append((0,0,1,0))
visited=[[[0]*m for _ in range(n)] for _ in range(2)]
directions=[(0,1),(0,-1),(1,0),(-1,0)]
while queue:
    #check는 이미 하나 부셨다는 표시
    y,x,d,check=queue.popleft()
    if y==n-1 and x==m-1:
        print(d)
        break
    for di in directions:
        dy=y+di[1]
        dx=x+di[0]
        # 범위 체크부터 먼저
        if 0<=dy<n and 0<=dx<m:
            if check == 1:
                # 이미 부신 애가 존재하면서 방문하지 않았고, graph==0인 경우
                # 이미 부신 적이 있으면 graph=0인 곳으로만 이동 가능
                if visited[check][dy][dx] == 0 and graph[dy][dx] == 0:
                    queue.append((dy, dx, d + 1, check))
                    visited[check][dy][dx] = 1
            else:
                # 아직 부신 적 없으면서 graph=1인 경우(벽인 경우)
                if graph[dy][dx] == 1 and visited[1][dy][dx] == 0:
                    queue.append((dy, dx, d + 1, 1))
                    visited[1][dy][dx]=1
                # 부신 적 없으면서 길인 경우
                elif graph[dy][dx] == 0 and visited[0][dy][dx] == 0:
                    queue.append((dy, dx, d + 1, 0))
                    visited[0][dy][dx] = 1
else:
    print(-1)