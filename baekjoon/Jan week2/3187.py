#3184번과 같은 문제
import sys
sys.setrecursionlimit(10**6)

wolf=0
sheep=0

def dfs(i,j):
    global wolf
    global sheep
    visited[i][j] = 1
    if field[i][j]=='v':
        wolf+=1
    elif field[i][j]=='k':
        sheep+=1

    di=[(1,0),(0,1),(-1,0),(0,-1)]
    for d in di:
        nx=i+d[0]
        ny=j+d[1]
        if 0<=nx<r and 0<=ny<c and visited[nx][ny]==0 and field[nx][ny]!='#':
            dfs(nx,ny)


r,c=list(map(int, input().split(' ')))
field=[]
for i in range(r):
    tmp=input()
    field.append(list(tmp))
visited=[[0 for _ in range(c)]for _ in range(r)]

total_wolf=0
total_sheep=0

for i in range(r):
    for j in range(c):
        if field[i][j]!='#' and visited[i][j]==0:
            wolf=0
            sheep=0
            dfs(i,j)
            if wolf>=sheep:
                total_wolf+=wolf
            elif wolf<sheep:
                total_sheep+=sheep

print(total_sheep, total_wolf)
