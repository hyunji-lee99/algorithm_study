# n : 통로의 세로 길이
# m : 통로의 가로 길이
# k : 음식물이 떨어진 좌표 개수
import sys
from collections import deque

#sys.setrecursionlimit(10**6)

n,m,k=map(int, sys.stdin.readline().split(' '))

corridor=[[0]*(m) for _ in range(n)]
for i in range(k):
    r,c=map(int, sys.stdin.readline().strip().split(' '))
    corridor[r-1][c-1]=1

visited=[[0]*(m) for _ in range(n)]
def dfs(i,j):
    global size
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    visited[i][j]=1
    size+=1
    for di in directions:
        dy=i+di[1]
        dx=j+di[0]
        if 0<=dy<n and 0<=dx<m and visited[dy][dx]==0 and corridor[dy][dx]==1:
            dfs(dy,dx)

def bfs(i,j):
    global size
    queue=deque()
    queue.append((i,j))
    visited[i][j]=1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        y,x=queue.popleft()
        size+=1
        for di in directions:
            dy=y+di[1]
            dx=x+di[0]
            if 0<=dy<n and 0<=dx<m and visited[dy][dx]==0 and corridor[dy][dx]==1:
                queue.append((dy,dx))
                visited[dy][dx]=1

ans=0
for i in range(n):
    for j in range(m):
        if corridor[i][j]==1 and visited[i][j]==0:
            size=0
            # dfs(i,j)
            bfs(i,j)
            ans=max(ans, size)

print(ans)




