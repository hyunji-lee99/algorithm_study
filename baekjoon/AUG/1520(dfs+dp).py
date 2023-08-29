import sys

h,w=map(int, sys.stdin.readline().strip().split(' '))
area=[list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(h)]

ans=0
directions=[(0,1),(1,0),(0,-1),(-1,0)]
DP=[[-1]*w for _ in range(h)]
# def dfs(y,x):
#     global ans, directions, visited, area
#     if y==h-1 and x==w-1:
#         ans+=1
#         return
#     visited[y][x]=1
#     for di in directions:
#         dy=y+di[0]
#         dx=x+di[1]
#         if 0<=dy<h and 0<=dx<w and visited[dy][dx]==0 and area[y][x]>area[dy][dx]:
#             dfs(dy,dx)
#     visited[y][x]=0


def dfs(y,x):
    if y==h-1 and x==w-1:
        return 1
    if DP[y][x]!=-1:
        return DP[y][x]
    DP[y][x]=0
    for di in directions:
        dy=y+di[0]
        dx=x+di[1]
        if 0<=dy<h and 0<=dx<w and area[y][x]>area[dy][dx]:
            DP[y][x]=DP[y][x]+dfs(dy,dx)
    return DP[y][x]


dfs(0,0)
print(DP[0][0])
