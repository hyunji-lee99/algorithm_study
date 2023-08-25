import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))

area=[[0]+list(map(int,sys.stdin.readline().strip().split(' '))) for _ in range(n)]
area.insert(0,[0]*(n+1))
visited=[[0]*(n+1) for _ in range(n+1)]
dest=[]

for i in range(1,m+1):
    y,x=map(int, sys.stdin.readline().strip().split(' '))
    dest.append((y,x))

directions=[(0,1),(1,0),(0,-1),(-1,0)]
ans=0

# def dfs(y,x,level):
#     global ans
#     if (y,x)==dest[level]:
#         if level==m-1:
#             ans+=1
#             return
#         else:
#             level+=1
#     visited[y][x] = 1
#     for di in directions:
#         dy=y+di[0]
#         dx=x+di[1]
#         if 1<=dy<=n and 1<=dx<=n and visited[dy][dx]==0 and area[dy][dx]==0:
#             dfs(dy,dx,level)
#     visited[y][x] = 0
#
# dfs(dest[0][0], dest[0][1], 1)

queue=deque()
visited[dest[0][0]][dest[0][1]]=1
queue.append((dest[0][0],dest[0][1],1,visited))
while queue:
    cury, curx, level, visited = queue.popleft()
    if cury==dest[level][0] and curx==dest[level][1]:
        if level==m-1:
            ans+=1
            continue
        else:
            level+=1
    for di in directions:
        dy=cury+di[0]
        dx=curx+di[1]
        if 1<=dy<=n and 1<=dx<=n and visited[dy][dx]==0 and area[dy][dx]==0:
            new_visited = [arr[:] for arr in visited]
            new_visited[dy][dx]=1
            queue.append((dy,dx,level,new_visited))


print(ans)