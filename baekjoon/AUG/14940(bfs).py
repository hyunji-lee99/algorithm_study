import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
area=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

visited = [[0] * (m) for _ in range(n)]
dist=[[0]*(m) for _ in range(n)]
def bfs(starty, startx):
    global visited, area, dist
    queue=deque()
    queue.append((starty, startx,0))
    visited[starty][startx]=1
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    while queue:
        y,x,d=queue.popleft()
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<m and visited[dy][dx]==0 and area[dy][dx]==1:
                queue.append((dy,dx,d+1))
                dist[dy][dx]=d+1
                visited[dy][dx]=1


# 시작 지점 찾기
for i in range(n):
    for j in range(m):
        if area[i][j]==2:
            bfs(i,j)
            # 출력하고,프로그램 종료
            for y in range(n):
                for x in range(m):
                    # 기존에 갈 수 있는 경로지만, 목적지에 도달할 수 없는 지역인 경우
                    if dist[y][x]==0 and area[y][x]==1:
                        dist[y][x]=-1
            for y in range(n):
                print(*dist[y], sep=' ')
            sys.exit(0)
