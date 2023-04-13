import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
area=[list(sys.stdin.readline()) for _ in range(n)]

land=[]
def bfs(y,x):
    global area
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    queue=deque()
    queue.append((y,x,0))
    visited=[[0]*m for _ in range(n)]
    visited[y][x]=1
    maxvalue=-1e9
    while queue:
        y,x,dist=queue.popleft()
        if maxvalue<dist:
            maxvalue=dist
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<m and visited[dy][dx]==0 and area[dy][dx]=='L':
                queue.append((dy,dx,dist+1))
                visited[dy][dx]=1
    return maxvalue


maxvalue=-1e9
visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if area[i][j]=='L' and visited[i][j]==0:
            maxvalue=max(bfs(i,j),maxvalue)
            visited[i][j]=1

print(maxvalue)


