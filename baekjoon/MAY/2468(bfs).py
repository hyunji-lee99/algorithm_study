import sys
from collections import deque

n=int(sys.stdin.readline())

info=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

max_height=max(max(arr for arr in info))
directions=[(1,0),(0,1),(-1,0),(0,-1)]

maxvalue=-1e9
for height in range(max_height+1):
    visited=[[0]*n for _ in range(n)]
    size=0
    for i in range(n):
        for j in range(n):
            # 방문한 적 없고, 비의 높이보다 큰 경우
            if visited[i][j]==0 and info[i][j]>height:
                size+=1
                #bfs
                queue=deque()
                queue.append((i,j))
                while queue:
                    y,x=queue.popleft()
                    for di in directions:
                        dy=y+di[0]
                        dx=x+di[1]
                        if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and info[dy][dx]>height:
                            queue.append((dy,dx))
                            visited[dy][dx]=1
    maxvalue = max(maxvalue, size)

print(maxvalue)




