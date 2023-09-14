import sys
from collections import deque

n,m=map(int, sys.stdin.readline().strip().split(' '))
present=[list(sys.stdin.readline().strip()) for _ in range(n)]
d=int(sys.stdin.readline())
future=[list(sys.stdin.readline().strip()) for _ in range(n)]

# future를 기준으로 기존의 present에 도달할 수 있는지 확인
queue=deque()
visited=[[0]*m for _ in range(n)]

def bfs_weed():
    global queue, visited, future
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    while queue:
        y,x=queue.popleft()
        for dy in range(y-d, y+d+1):
            for dx in range(x-d, x+d+1):
                if 0 <= dy < n and 0 <= dx < m and visited[dy][dx] == 0 and future[dy][dx] == 'O' and abs(y-dy)+abs(x-dx)<=d:
                    queue.append((dy, dx))
                    visited[dy][dx] = 1

for i in range(n):
    for j in range(m):
        if present[i][j]=='O' and visited[i][j]==0:
            queue.append((i,j))
            visited[i][j]=1
            bfs_weed()

for i in range(n):
    for j in range(m):
        if (future[i][j]=='O' and visited[i][j]==0) or (future[i][j]=='X' and present[i][j]=='O'):
            print('NO')
            sys.exit(0)

print('YES')