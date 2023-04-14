import sys
from collections import deque

cnt=1
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    cave=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    queue=deque()
    queue.append((0,0))
    visited=[[1e9]*n for _ in range(n)]
    visited[0][0]=cave[0][0]
    while queue:
        y,x=queue.popleft()
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<n:
                if visited[dy][dx]>visited[y][x]+cave[dy][dx]:
                    queue.append((dy, dx))
                    visited[dy][dx] = visited[y][x]+cave[dy][dx]
    print('Problem '+str(cnt)+': '+str(visited[n-1][n-1]))
    cnt+=1